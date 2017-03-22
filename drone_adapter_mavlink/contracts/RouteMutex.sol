pragma solidity ^0.4.9;

contract RouteMutex {
    struct Route {
        address owner;
        string route;
    }

    mapping (bytes32 => Route) routeOf;
    
    function get(string _ipfs_hash) constant returns (address, string) {
        var route = routeOf[sha3(_ipfs_hash)];
        return (route.owner, route.route);
    }

    function acquire(string _ipfs_hash) {
        if (routeOf[sha3(_ipfs_hash)].owner == 0) {
            routeOf[sha3(_ipfs_hash)] = Route(msg.sender, _ipfs_hash);
        } else {
            throw;
        }
    }
    
    function release(string _ipfs_hash) {
        if (routeOf[sha3(_ipfs_hash)].owner == msg.sender) {
            delete routeOf[sha3(_ipfs_hash)];
        } else {
            throw;
        }
    }
}
