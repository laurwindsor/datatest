SELECT bis.sessionsid AS sessionsid,
       bis.entrydate AS entrydate
FROM bi_sessions bis
WHERE entrydate > '2017-01-01'
LIMIT 25
;