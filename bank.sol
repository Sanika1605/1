
//SPDX-License-Identifier:MIT
pragma solidity ^0.8.0;
contract Bank{
    address public accHolder;
    uint256 public balance;
    constructor() {
        accHolder=msg.sender;
    }
    function withdraw() public payable{
        require(balance >=msg.value,"Insufficient Balance");
        payable(msg.sender).transfer(msg.value);
        balance-=msg.value;
    }
    function deposit() public payable{
        require(msg.value>0,"Deposit amount must be greater then 0");
        balance+=msg.value;
    }
    function showBalance() public view returns (uint256){
        return balance;
    }
}
