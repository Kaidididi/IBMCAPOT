USE `sql_50`;

-- 查询平均成绩大于或等于60分的学生编号、姓名和平均成绩

select a.sid,
b.Sname,
avgs
from(
select SId,
AVG(score) as avgs 
from sc
group by Sid 
having AVG(Score) >=60
)a
left join student b
on a.sid = b.sid;





select s.*,sc.CID, sc.score from student s  
left join sc on s.SId=sc.SId 
where s.SId in(select a.SId FROM (
select *from sc where CId=01)a  INNER JOIN  (
select *from sc where CId=02
)b ON a.SId=b.SId where a.score>b.score group by a.SId);