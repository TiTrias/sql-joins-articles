<?php

$jsondata = file_get_contents("config.json");
$config = json_decode($jsondata,true);

$servername = $config["mydb"]["host"];
$username = $config["mydb"]["user"];
$password = $config["mydb"]["password"];
$dbname = $config["mydb"]["database"];

$GLOBALS['numberOfExecutions'] = 3;
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
function executeSQLEchoTime($conn,$sql,$message = ''){
    $minStep=0;
    $maxStep=0;
    $totalTime=0;
    for ($i = 1; $i <= $GLOBALS['numberOfExecutions']; $i++) {
        echo $i . "\n" ;
        $t1 = microtime(true);
        $result = $conn->query($sql);
        $t2 = microtime(true);
        $timeStep = ($t2 - $t1);
        if($i==1){
            $minStep = $timeStep;
            $maxStep = $timeStep;

        }
        if($timeStep<$minStep){
            $minStep = $timeStep;
        }
        if($timeStep>$maxStep){
            $maxStep = $timeStep;
        }        
        $totalTime += $timeStep;
    }
    
    
    
    $time = $totalTime / $GLOBALS['numberOfExecutions'];
    


    echo sprintf('Average Execution time for [%s] after %f executions = %f, Max = %f, Min= %f ',$message,$GLOBALS['numberOfExecutions'], $time,$maxStep,$minStep) . "\n";
    
}

// Create connection
$sqlInnerWhere = "SELECT SQL_NO_CACHE * from Department, Employee, EmployeeBonus
WHERE Department.ID = Employee.DepartmentID
AND Employee.SSN = EmployeeBonus.EmployeeSSN;";

$sqlInnerOn = "SELECT SQL_NO_CACHE * from Department 
INNER JOIN Employee ON Department.ID = Employee.DepartmentID
INNER JOIN EmployeeBonus ON Employee.SSN = EmployeeBonus.EmployeeSSN;";


$sqlOuterLeftEmpDept = "SELECT SQL_NO_CACHE Employee.SSN, Employee.Name as 'Employee Name', Department.Name as 'Department Name', Department.Email as 'Department Email'
FROM Employee  
LEFT OUTER JOIN Department ON Department.ID = Employee.DepartmentID;";

$sqlOuterLeftEmpBonus = "SELECT SQL_NO_CACHE Employee.SSN, Employee.Name as 'Employee Name', EmployeeBonus.Reason , EmployeeBonus.BonusDate,EmployeeBonus.Value 
FROM Employee 
LEFT OUTER JOIN EmployeeBonus  ON Employee.SSN = EmployeeBonus.EmployeeSSN;";

$sqlOuterRightEmpDept = "SELECT SQL_NO_CACHE Employee.SSN, Employee.Name as 'Employee Name', Department.Name as 'Department Name', Department.Email as 'Department Email'
FROM Employee  
Right OUTER JOIN Department ON Department.ID = Employee.DepartmentID;";


// executeSQLEchoTime($conn,$sqlInnerOn,'INNER JOIN by INNERJOIN');
// executeSQLEchoTime($conn,$sqlInnerWhere,'INNER JOIN by WHERE');

// executeSQLEchoTime($conn,$sqlInnerOn,'LEFT OUTER JOIN Employee-Department');
// executeSQLEchoTime($conn,$sqlInnerWhere,'LEFT OUTER JOIN Employee-Bonus');

executeSQLEchoTime($conn,$sqlOuterRightEmpDept,'RIGHT OUTER JOIN Employee-Department');


$conn->close();
?>
