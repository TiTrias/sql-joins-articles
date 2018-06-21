SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `EmployeesDBArticle`
--

-- --------------------------------------------------------

--
-- Table structure for table `Department`
--

CREATE TABLE `Department` (
  `ID` int(11) NOT NULL,
  `Name` text NOT NULL,
  `Email` text NOT NULL,
  `Phone` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Department`
--

INSERT INTO `Department` (`ID`, `Name`, `Email`, `Phone`) VALUES
(1, 'IT', 'it@example.com', '(005)-555 5555'),
(2, 'Sales', 'sales@example.com', '(005)-555 5556'),
(3, 'HR', 'hr@example.com', '(005)-555 5557');

-- --------------------------------------------------------

--
-- Table structure for table `Employee`
--

CREATE TABLE `Employee` (
  `SSN` char(11) NOT NULL,
  `Name` text NOT NULL,
  `Mobile` text NOT NULL,
  `Birthdate` date NOT NULL,
  `DepartmentID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Employee`
--

INSERT INTO `Employee` (`SSN`, `Name`, `Mobile`, `Birthdate`, `DepartmentID`) VALUES
('001-01-1933', 'Bob', '(005)-015 4567', '1981-08-21', 1),
('004-02-1543', 'Alice', '(005)-013 5678', '1972-01-01', NULL),
('009-02-1422', 'Dan', '(005)-014 9876', '1993-03-27', 2);

-- --------------------------------------------------------

--
-- Table structure for table `EmployeeBonus`
--

CREATE TABLE `EmployeeBonus` (
  `EmployeeSSN` char(11) NOT NULL,
  `Reason` text NOT NULL,
  `BonusDate` date NOT NULL,
  `Value` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `EmployeeBonus`
--

INSERT INTO `EmployeeBonus` (`EmployeeSSN`, `Reason`, `BonusDate`, `Value`) VALUES
('001-01-1933', 'Over time', '2017-05-05', 100),
('001-01-1933', 'Early delivery', '2017-05-07', 150),
('004-02-1543', 'Travelling', '2017-05-08', 500);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Department`
--
ALTER TABLE `Department`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Department`
--
ALTER TABLE `Department`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
