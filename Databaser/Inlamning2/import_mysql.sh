read -p "Enter username: " username
read -p "Enter database name: " database_name

mysql -u $username -p $database_name < ./bank_accounts.sql
