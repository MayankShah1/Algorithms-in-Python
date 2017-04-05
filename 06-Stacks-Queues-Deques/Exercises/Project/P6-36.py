import arrayqueue as Queue

def capital_gain():

    raw = 'start'
    queue_num = Queue.ArrayQueue()
    queue_amount = Queue.ArrayQueue()
    while raw != '' or raw != '\n':
        raw = input('Enter transaction details: \n')
        tokens = raw.split(' ')

        if len(tokens) < 2:
            break

        task = tokens[0]

        total_shares = 0

        if task == 'buy':
            queue_num.enqueue(int(tokens[1]))
            total_shares += int(tokens[1])
            amt = tokens[4]
            queue_amount.enqueue(int(amt[1:]))
        else:
            num_sold = int(tokens[1])
            amt = tokens[4]
            amt_sold = int(amt[1:])

            capital_res = 0

            while num_sold > 0 or not queue_num.is_empty():
                stock_num = queue_num.dequeue()
                if stock_num <= num_sold:
                    num_sold -= stock_num
                    capital_res += (amt_sold-queue_amount.dequeue())*stock_num
                else:
                    capital_res += num_sold * (amt_sold-queue_amount.dequeue())
                    num_sold = 0

    return capital_res


# Testing
if __name__ == "__main__":
    print(capital_gain())