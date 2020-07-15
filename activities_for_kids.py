def run(*kids):
    for kid in kids:
        print(f'{kid} was running around.')

def swing(*kids):
    for kid in kids:
        print(f'{kid} was swinging on the swingset.')

def slide(*kids):
    for kid in kids:
        print(f'{kid} slid down the slides.')

def hide_and_seek(*kids):
    for kid in kids:
        print(f'{kid} played hide and seek.')

run("Pam", "Sam", "Andrea", "Will")
swing("Marybeth", "Ariel", "Kevin", "Courtney")
slide("Mike", "Jack", "Jennifer", "Earl")
hide_and_seek("Henry", "Heather", "Hayley", "Hugh")