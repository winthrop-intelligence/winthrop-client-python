"""Contract tests for the generated CTB compensation exception client."""

from datetime import date, datetime, timezone

import pytest
from pydantic import ValidationError

from winthrop_client_python.api_client import ApiClient
from winthrop_client_python.models.ctb_compensation_processing_event_input import (
    CtbCompensationProcessingEventInput,
)
from winthrop_client_python.models.ctb_compensation_processing_event_request import (
    CtbCompensationProcessingEventRequest,
)
from winthrop_client_python.models.ctb_compensation_processing_event_response import (
    CtbCompensationProcessingEventResponse,
)
from winthrop_client_python.models.ctb_compensation_expected_request import (
    CtbCompensationExpectedRequest,
)
from winthrop_client_python.models.foia_inbox_expected_compensation import (
    FoiaInboxExpectedCompensation,
)
from winthrop_client_python.models.foia_inbox_expected_position import (
    FoiaInboxExpectedPosition,
)
from winthrop_client_python.models.foia_inbox_expected_requested_item import (
    FoiaInboxExpectedRequestedItem,
)

SHA_A = "a" * 64
SHA_B = "b" * 64
SHA_C = "c" * 64
UPDATED_AT = datetime(2026, 7, 24, 18, 30, tzinfo=timezone.utc)
ALL_ACTIONS = [
    "update_requested_item_status",
    "add_requested_item_note",
    "update_compensation_status",
    "add_compensation_note",
    "add_position_type",
]


def request_input(**overrides) -> CtbCompensationProcessingEventInput:
    values = {
        "idempotency_key": "ctb-review-123",
        "review_series_id": "ctb-folder-44",
        "review_revision_sha256": SHA_A,
        "decision_sha256": SHA_B,
        "foia_request_id": 201,
        "school_id": 44,
        "requested_item_id": 101,
        "compensation_id": 501,
        "role": "volunteer",
        "actions": ALL_ACTIONS,
        "expected_request": CtbCompensationExpectedRequest(
            status="ACTIVE",
            updated_at=UPDATED_AT,
            updated_by_school=date(2026, 7, 1),
            updated_by_wi=None,
            foia_notes_sha256=SHA_C,
        ),
        "expected_requested_item": FoiaInboxExpectedRequestedItem(
            status="pending",
            updated_at=UPDATED_AT,
            ri_note_sha256=SHA_A,
        ),
        "expected_compensation": FoiaInboxExpectedCompensation(
            year=2027,
            school_id=44,
            coach_id=701,
            contract_status="AVAILABLE",
            comment=None,
            updated_at=UPDATED_AT,
            positions_sha256=SHA_B,
            positions=[
                FoiaInboxExpectedPosition(
                    position_id=801,
                    coach_id=701,
                    school_id=44,
                    year=2027,
                    position_type_ids=[9],
                )
            ],
        ),
    }
    values.update(overrides)
    return CtbCompensationProcessingEventInput(**values)


def test_request_round_trip_preserves_granular_actions_and_snapshots():
    request = CtbCompensationProcessingEventRequest(
        ctb_compensation_processing_event=request_input()
    )

    serialized = ApiClient().sanitize_for_serialization(request)
    event = serialized["ctb_compensation_processing_event"]

    assert event["role"] == "volunteer"
    assert event["actions"] == ALL_ACTIONS
    assert event["expected_request"]["updated_by_wi"] is None
    assert event["expected_requested_item"]["status"] == "pending"
    assert event["expected_compensation"]["positions"][0] == {
        "position_id": 801,
        "coach_id": 701,
        "school_id": 44,
        "year": 2027,
        "position_type_ids": [9],
    }

    restored = CtbCompensationProcessingEventRequest.from_dict(serialized)
    assert restored == request


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("role", "foundation_employee"),
        ("actions", ["update_requested_item_status", "delete_position"]),
    ],
)
def test_request_rejects_unknown_role_and_action_enums(field, value):
    with pytest.raises(ValidationError):
        request_input(**{field: value})


def test_response_round_trip_preserves_idempotency_and_applied_subset():
    payload = {
        "id": 9001,
        "idempotency_key": "ctb-review-123",
        "review_series_id": "ctb-folder-44",
        "review_revision_sha256": SHA_A,
        "decision_sha256": SHA_B,
        "request_sha256": SHA_C,
        "foia_request_id": 201,
        "school_id": 44,
        "requested_item_id": 101,
        "compensation_id": 501,
        "status": "applied",
        "applied_at": "2026-07-24T18:31:00Z",
        "result": {
            "review_series_id": "ctb-folder-44",
            "review_revision_sha256": SHA_A,
            "decision_sha256": SHA_B,
            "compensation_exception": {
                "requested_item_id": 101,
                "compensation_id": 501,
                "role": "not_employed",
                "actions": [
                    "update_requested_item_status",
                    "add_requested_item_note",
                    "update_compensation_status",
                ],
            },
        },
        "idempotent": True,
    }

    response = CtbCompensationProcessingEventResponse.from_dict(payload)

    assert response.to_dict()["result"]["compensation_exception"]["actions"] == [
        "update_requested_item_status",
        "add_requested_item_note",
        "update_compensation_status",
    ]
    assert response.idempotent is True
    assert CtbCompensationProcessingEventResponse.from_dict(
        ApiClient().sanitize_for_serialization(response)
    ) == response
