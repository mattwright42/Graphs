import random
from queue import *


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(f"User {i+1}")

        # create friendships
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))
        random.shuffle(possibleFriendships)
        print(possibleFriendships)
        print(len(possibleFriendships))

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        # Create an empty set of visited vertices
        # Put the starting vertex in our Queue
        q.put(userID)
        # While the queue is not empty...
        while q.qsize() > 0:
            # Dequeue the first node from the queue
            path = []
            path.append(q.get())  # this is the path
            # If that node has not been visited...
            print("path: ", path)
            v = path[-1]
            if v not in visited:
                # Mark it as visited
                visited[v] = path
                print("visited: ", visited)
                print("friendships: ", self.friendships)

                for friendship in self.friendships[v]:
                    new_path = self.friendships[v]
                    print("new_path: ", new_path)
                    new_path.add(friendship)
                    print("new_path2: ", new_path)
                    q.put(friendship)

        print("visited: ", visited)
        return visited
        # return self.getAllSocialPaths(userID + 1)


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    sg.addFriendship(1, 2)
    sg.addFriendship(3, 7)
    sg.addFriendship(5, 2)
    sg.addFriendship(1, 2)
    sg.addFriendship(1, 5)
    sg.addFriendship(1, 7)
    sg.addFriendship(4, 9)
    sg.addFriendship(4, 5)
    sg.addFriendship(6, 1)
    connections = sg.getAllSocialPaths(1)

# 10 choose 2
# n! / 2 * (n - 2)!
# n! = n * (n - 1)  * (n - 2)!
#n * (n - 1)
#O(n ^ 2)

[1, 2]
[1, 3]
[1, 4]
[1, 5]
[1, 6]
[1, 7]
[1, 8]
[1, 9]
[1, 10]

[2, 3]
[2, 4]
[2, 5]
[2, 6]
[2, 7]
[2, 8]
[2, 9]
[2, 10]
