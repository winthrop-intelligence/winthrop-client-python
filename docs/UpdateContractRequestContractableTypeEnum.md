# UpdateContractRequestContractableTypeEnum

Sets the owner type (WINAD-10739), for example to repair a contract saved with a contractable_id and no type. Only Coach is accepted. A contract with no owner id needs coach_id / contractable_id in the same request, because the type alone is a 422 (errors.contractable_id). Together with coach_id / contractable_id these are the only fields a pending contract accepts.

## Enum

* `COACH` (value: `'Coach'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


