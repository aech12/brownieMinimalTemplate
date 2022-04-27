// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Store {
    struct User {
        uint256 favoriteNumber;
        string name;
    }

    uint256 favoriteNumber;
    User[] public users;
    mapping(string => uint256) public nameToFavoriteNumber;

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    function addUser(string memory _name, uint256 _favoriteNumber) public {
        users.push(User(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
