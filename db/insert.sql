
\c pes_interconnect2


insert into club values(1,'IEEE PESU'),
(2,'TEDX'),
(3,'pixelloid'),
(4,'hash code'),
(5,'equinox'),
(6,'rotaract club'),
(7,'A CORD club'),
(8,'action cut'),
(9,'bhushaaritih'),
(10,'rotaract club');


insert into staff values(1,'prochancellor@pes.edu','jawahar doreswamy','pro chaCncellor'), 
(2,'vkrishna@pes.edu','v krishna','vice chancellor'),
(3,'laksmanks@pes.edu','laksman ks','accounting_head'),
(4,'manjunathreddy@pes.edu','manjunath reddy','coe_head'),
(5,'dineshsingh@pes.edu','dineshsingh','student dean'),
(6,'manjeetsingh@pes.edu','manjeet singh','sports head'),
(7,'library@pes.edu','rajesh kumar','librarian'),
(8,'shivashakar@pes.edu','shiva shakar','boys hostel warden'),
(9,'ropalis@pes.edu','ropali shankar ','girls hostel warden'),
(10,'raghub@pes.edu','raghu b','housekeeping staff head');


insert into section values(203, 1, 'G');
insert into section values(301, 2, 'H');
insert into section values(302, 2, 'I');
insert into section values(401, 3, 'J');
insert into section values(201, 1, 'E');
insert into section values(202, 1, 'F');
insert into section values(101, 0, 'A');
insert into section values(102, 0, 'B');
insert into section values(103, 0, 'C');
insert into section values(104, 0, 'D');


insert into Teacher values(1,'raghavk@pes.edu','raghav kumar ',9765843595,'no 65 JP nagar bangalore',3),
(2,'radhakrishna@pes.edu','radha krishna ',9765748595,'no34 RR nagar bangalore',5),
(3,'harishks@pes.edu','harish k s ',9765847895,'no 34 Jaynagar  bangalore',null),
(4,'sivareddy@pes.edu','shiva reddy ',9765843595,'no25 basavanagudi  bangalore',8),
(5,'preetp@pes.edu','preet p',9765568357,'no24 malashwaram  bangalore',null),
(6,'dinashsingh@pes.edu','dinesh singh ',9764683595,'no 12 JP nagar bangalore',9),
(7,'anilkumar@pes.edu','anil kumar ',9765387595,'no13 shanti  nagar bangalore',7),
(8,'siviraman@pes.edu','siviraman ',9765674595,'no17 vv puram bangalore',6),
(9,'surayaprakash@pes.edu','surya prakash',9767393595,'no65 BTM layout bangalore',3),
(10,'mahemag@pes.edu','mahema g ',9765847995,'no34 kr road bangalore',null);


insert into course values(1,'DBMS',4,'core',2),
(2,'WT',4,'core',4),
(3,'MI',4,'core',3),
(4,'ARVR',4,'elective',1),
(5,'MPCA',4,'core',5),
(6,'GTA',4,'elective',7),
(7,'java',2,'special',6),
(8,'IOT',2,'special',10),
(9,'android',2,'special',8),
(10,'robotics',2,'special',9);



insert into department values('computer science department','cse@pes.edu',1,26679976,'0-2',5),
('electronics and communication department','ece@pes.edu',2,27657976,'3-5',7),
('electronics electeical department','eee@pes.edu',3,26873876,'6-7',2),
('mechanical department','mech@pes.edu',4,28779976,'8-8',1),
('civil department ','cve@pes.edu',5,45789456,'9-10',3),
('architecture department','arch@pes.edu',6,47837786,'11-12',8);


insert into student values('abhinav pai',1,'n0 55 jaynagar bangalore ',9692564564,8.54,'abhinavpai200@gmail.com', 'A', 1, 1),
('abhishak pai',2,'n0 17 HSR layout bangalore ',9574458604,8.9,'abhishakpai46@gmail.com', 'B', 2, 2),
('akshitha reddy',3,'n0 18 BTM layout bangalore ',9558788604,8.48,'akshithareddy34@gmail.com', 'C', 3, 3),
('chirag  singavi',4,'n0 55 MG road bangalore ',9697855604,7.94,'chiragsingavi20@gmail.com', 'D', 4, 5),
('disha jain',5,'n0 34 jaynagar bangalore ',9784648604,7.95,'dishajain67@gmail.com', 'E', 5, 4),
('dhanush venkatesh',6,'n0 45 basavanagudi bangalore ',9692754564,8.54,'dhanushvenkatesh200@gmail.com', 'F', 6, 1),
('harsh kumar',7,'n0 55 VV puram bangalore ',9694789604,6.78,'harshkumar35@gmail.com', 'J', 3, 5),
('naman bhandari',8,'n0 56 shanti nagar bangalore ',9694376604,7.54,'namanrock35@gmail.com', 'G', 1, 9),
('pratik p',9,'n0 45 BTM layout  bangalore ',9692796564,9.78,'pratikp20@gmail.com', 'H', 1, 10),
('srinivas v',10,'n0 45 girinagar bangalore ',9692785664,9.54,'srinivasv56@gmail.com', 'I', 2, 1);


insert into consists values(2,1),(1,2),(2,3),(4,3),(9,5),(10,4),(7,6),(8,10),(9,2),(3,7);


insert into teaches values(2,1,1),(1,2,1),(4,3,1),(3,4,2),(9,5,2),(10,6,2),(8,7,3),(7,8,4),(6,9,5),(5,10,6);


insert into opts values(2,1),(1,2),(2,3),(3,4),(2,5),(3,6),(2,7),(7,8),(6,9),(5,10);


insert into managed_by values(3, 9);
insert into managed_by values(5, 10);
insert into managed_by values(1, 1);
insert into managed_by values(1, 2);
insert into managed_by values(1, 3);
insert into managed_by values(1, 4);
insert into managed_by values(2, 4);
insert into managed_by values(2, 6);
insert into managed_by values(4, 8);
insert into managed_by values(5, 7);


insert into offers values(1,1);
insert into offers values(1,2);
insert into offers values(1,3);
insert into offers values(1,4);
insert into offers values(2,1);
insert into offers values(2,5);
insert into offers values(2,6);
insert into offers values(3,7);
insert into offers values(4,8);
insert into offers values(5,9);
insert into offers values(6,10);


insert into tutors values(1, 'A');
insert into tutors values(2, 'B');
insert into tutors values(3, 'C');
insert into tutors values(4, 'D');
insert into tutors values(5, 'E');
insert into tutors values(6, 'F');
insert into tutors values(7, 'G');
insert into tutors values(8, 'H');
insert into tutors values(9, 'I');
insert into tutors values(10, 'J');
