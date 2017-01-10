<?php 

//include('../db/connect.php');

//get total sum from the database

$sql = "select sum(CumulativePatients) treatments from AidStations;";

$result = $db->query($sql);
if ($result->num_rows==1){
    $row = $result -> fetch_assoc();
    $treatments =$row['treatments'];
}
echo "<script> var totalTreatments = $treatments; </script>";

$sql_current = "select sum(CurrentPatients) currentTreatments from AidStations;";

$result_current = $db->query($sql_current);
if ($result_current->num_rows==1){
    $row = $result_current -> fetch_assoc();
    $treatments_current =$row['currentTreatments'];
}
echo "<script> var inMedical = $treatments_current; </script>";

?>
