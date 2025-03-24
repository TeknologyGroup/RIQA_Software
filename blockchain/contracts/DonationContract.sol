// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DonationContract {
    address public owner;
    uint256 public totalDonations;

    constructor() {
        owner = msg.sender;
    }

    function donate() external payable {
        totalDonations += msg.value;
    }
}