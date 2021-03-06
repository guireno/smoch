# Integration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The integration ID, generated automatically. | 
**type** | **str** | The integration type. | 
**page_access_token** | **str** | Facebook Page Access Token. Required for *messenger* integrations.  | [optional] 
**app_id** | **str** | Facebook App ID OR WeChat App ID. Required for *messenger* and *wechat* integrations.  | [optional] 
**app_secret** | **str** | Facebook Page App Secret OR WeChat App Secret. Required for *messenger* and *wechat* integrations.  | [optional] 
**account_sid** | **str** | Twilio Account SID. Required for *twilio* integrations.  | [optional] 
**auth_token** | **str** | Twilio Auth Token. Required for *twilio* integrations.  | [optional] 
**phone_number_sid** | **str** | SID for specific phone number. Required for *twilio* integrations.  | [optional] 
**token** | **str** | Telegram Bot Token OR Viber Public Account token. Required for *twilio* and *viber* integrations.  | [optional] 
**channel_access_token** | **str** | LINE Channel Access Token. Required for *line* integrations.  | [optional] 
**encoding_aes_key** | **str** | AES Encoding Key. (Optional) Used for *wechat* integrations.  | [optional] 
**from_address** | **str** | Email will display as coming from this address. (Optional) Used for *frontendEmail* integrations.  | [optional] 
**certificate** | **str** | The binary of your APN certificate base64 encoded. Required for *apn* integrations.  | [optional] 
**password** | **str** | The password for your APN certificate. (Optional) Used for *apn* integrations.  | [optional] 
**auto_update_badge** | **bool** | Use the unread count of the conversation as the application badge. (Optional) Used for *apn* integrations.  | [optional] 
**server_key** | **str** | Your server key from the fcm console. Required for *fcm* integrations.  | [optional] 
**sender_id** | **str** | Your sender id from the fcm console. Required for *fcm* integrations.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


