use houston2016;
select minute, position DIV 5 segment, count(*) total from MarathonRunners where dropout=0 and half=1 group by minute,segment;  