# ALGORITHM:
# If the monkey is clever enough, he can come to the block, drag 
# the block to the center, climb on it, and get the banana. Below 
# are few observations in this case − 
# 1. Monkey can reach the block, if both of them are at the same level. From the above 
# image, we can see that both the monkey and the block are on the floor. 
# 2. If the block position is not at the center, then the monkey can drag it to the center. 
# 3. If the monkey and the block both are on the floor, and the block is at the center, then 
# the monkey can climb up on the block. So the vertical position of the monkey will 
# be changed. 
# 4. When the monkey is on the block, and the block is at the center, then the monkey 
# can get the bananas. 





problem = {
 "start": ["at door", "on floor", "has ball", "hungry", "chair at door"],
 "finish": ["not hungry"],
 "ops": [
 {
 "action": "climb on chair",
 "preconds": ["chair at middle room", "at middle room", "on floor"],
 "add": ["at bananas", "on chair"],
 "delete": ["at middle room", "on floor"]
 },
 {
 "action": "push chair from door to middle room",
 "preconds": ["chair at door", "at door"],
 "add": ["chair at middle room", "at middle room"],
 "delete": ["chair at door", "at door"]
 },
 {
 "action": "walk from door to middle room",
 "preconds": ["at door", "on floor"],
 "add": ["at middle room"],
 "delete": ["at door"]
 },
 {
 "action": "grasp bananas",
 "preconds": ["at bananas", "empty handed"],
 "add": ["has bananas"],
 "delete": ["empty handed"]
 },
 {
 "action": "drop ball",
 "preconds": ["has ball"],
 "add": ["empty handed"],
 "delete": ["has ball"]
 },
 {
 "action": "eat bananas",
 "preconds": ["has bananas"],
 "add": ["empty handed", "not hungry"],
 "delete": ["has bananas", "hungry"]
 }
 ]
}
def main():
    start = problem['start']
    finish = problem['finish']
    ops = problem['ops']
    for action in (start, finish, ops):
        print(action)

if __name__ == '__main__':
    main()