import sqlite3

new = True
highest = 2
new_id = 2

connection = sqlite3.connect("test.db")
print(connection.total_changes)

cursor = connection.cursor()

try:
    cursor.execute("SELECT * FROM primes")
    rows = cursor.fetchall()
    for row in rows:
        if row[0] == 0:
            new = False
            highest = row[1]
            new_id = row[2]

except:  # noqa: E722
    pass

if new:
    cursor.execute("CREATE TABLE IF NOT EXISTS primes (id INTEGER, Prime INTEGER, maxid INTEGER)")
    cursor.execute("INSERT INTO primes VALUES (0, '1', 2)")
    cursor.execute("INSERT INTO primes VALUES (1, '1', 0)")


connection.commit()
connection.close()

def check_prime(Number):
    is_prime = True
    
    for i in range(Number):
        n = i + 2
        
        if n < Number:
            if int(Number / n) - Number / n == 0:
                is_prime = False
                break
        else:
            break
        
    return is_prime, Number

def main():
    while True:
        global highest
        global new_id
        
        prime, Number = check_prime(highest)
        
        connection = sqlite3.connect("test.db")
        cursor = connection.cursor()
        
        if prime:
            cursor.execute(f"INSERT INTO primes VALUES ({new_id}, {Number}, 0)")
            cursor.execute(f"UPDATE primes SET maxid = {new_id + 1} WHERE id = 0")
            new_id += 1
            
        else:
            cursor.execute(f"UPDATE primes SET Prime = {highest} WHERE id = 0")

        connection.commit()
        connection.close()
        
        highest += 1
        
if __name__ == "__main__":
    main()