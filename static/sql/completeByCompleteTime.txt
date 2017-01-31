SELECT bic.sessionid AS sessionid,
       bic.completetime AS completetime
FROM bi_completes bic
WHERE completetime > '2017-01-01'
LIMIT 25
;