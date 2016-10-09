-- Tweets written by users
select *,
COALESCE(en, 0) + COALESCE(lv, 0) + COALESCE(ru, 0) as total,
round(
        0.5 - abs(
        (
            (COALESCE(lv, 0) + 0.0) /
            (
                COALESCE(lv, 0.00001) +
                COALESCE(ru, 0.00001)
            )
        )
            - 0.5
    ),
    2
) as score
from crosstab(
    $$
	select
	screen_name#>>'{}',
	tweet->>'lang' as lang,
	count(*) as count
	from tweet, jsonb_array_elements(features->'screen_names') screen_name
	group by screen_name, lang
	order by 1;
    $$,
    $$
    select distinct tweet->>'lang' from tweet where tweet->>'lang' in ('en', 'ru', 'lv')
 order by 1
    $$
)
as final_result(screen_name text, en bigint, lv bigint, ru bigint)
order by score desc, total desc, screen_name