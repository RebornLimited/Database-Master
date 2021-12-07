# Database-Master
#### Manage your database with a user-friendly and intuitive interface.

### Usage:
<ol>
  <li>Run the <a href="DatabaseMaster.py">DatabaseMaster.py</a> file as a program (double click on the file).</li>
  <li>Enter data from the database.</li>
  <li>In the Request field, enter the SQL command.</li>
  <li>Click on the Done button.</li>
</ol>

### Examples of SQL commands:
1. Creating a table - ```CREATE TABLE `users`(id int AUTO_INCREMENT, name varchar(32), password varchar(32), PRIMARY KEY (id));```
2. Adding data to a table - ```INSERT INTO `users` (name, password) VALUES ('Jack', '12345');```
3. Changing data in a table - ```UPDATE `users` SET password = '6789and10' WHERE id = 1;```
4. Removing data from a table - ```DELETE FROM `users` WHERE id = 1;```
5. Dropping a table - ```DROP TABLE `users`;```
