-- models/my_model.sql
with source_data as (
    select * from {{ source('public', 'cleaned_data') }}
)

select
    channel_id,
    msg_id,
    lower(channel_name) as channel_name,
    lower(message) as message,
    lower(cleaned_message) as cleaned_message,
    to_timestamp(date, 'YYYY-MM-DD HH24:MI:SS') as date,
    msg_link,
    views,
    number_replies,
    number_forwards,
    is_forward,
    is_reply,
    contains_media,
    lower(media_type) as media_type,
    has_url
from source_data
