// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SoulboundToken {
    string public name = "BlackBoxSBT";
    string public symbol = "BBSBT";
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function getOwner() public view returns (address) {
        return owner;
    }

    // Prevent transfer
    function transfer(address _to) public pure {
        revert("Soulbound tokens cannot be transferred.");
    }
}
