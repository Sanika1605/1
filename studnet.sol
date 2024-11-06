// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    struct Student {
        uint id;
        string name;
        uint age;
        address studentAddress; // Changed to studentAddress for consistency
    }

    address public owner;
    Student[] public students;

    event StudentAdded(uint id, string name, uint age, address studentAddress); // Changed to StudentAdded for consistency

    constructor() {
        owner = msg.sender;
    }

    function addStudent(uint _id, string memory _name, uint _age, address _studentAddress) public {
        students.push(Student(_id, _name, _age, _studentAddress));
        emit StudentAdded(_id, _name, _age, _studentAddress);
    }

    function getStudent(uint _index) public view returns (uint, string memory, uint, address) {
        // Check if the index is valid
        require(_index < students.length, "Invalid index"); // Ensuring the index is valid
        Student storage student = students[_index];
        return (student.id, student.name, student.age, student.studentAddress);
    }

    fallback() external payable {
        payable(owner).transfer(address(this).balance);
    }

    receive() external payable {}
}
