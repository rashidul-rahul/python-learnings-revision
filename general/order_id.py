import datetime

ORDER_ID = "0311032342403BD"


class OrderIdGenerator:
    last_item = None
    last_date = None

    def check_num(self, num):
        if len(str(num)) == 1:
            return f"0{num}"
        else:
            return num

    def update_from_old_order(self, order_id):
        year = datetime.datetime.today().year
        try:
            _, item_number = order_id.split(str(year))
            item_number = item_number.replace("BD", "")
            print(int(order_id[:2]))
            if int(order_id[:2]) != datetime.datetime.today().day:
                self.last_date = datetime.datetime.today().day
                self.last_item = 0
            else:
                self.last_item = int(item_number)
                self.last_date = int(order_id[:2])
        except Exception as e:
            print(e)
            self.last_item = 0
            self.last_date = datetime.datetime.today().day

    def update_item_number(self):
        day = datetime.datetime.today().day
        if self.last_item and self.last_date:
            if self.last_date != day:
                self.last_date = day
                self.last_item = 1

        else:
            order_id = ORDER_ID
            self.update_from_old_order(order_id)

    def generate_order_id(self):
        self.update_item_number()
        order_id = f"{self.check_num(self.last_date)}{self.check_num(datetime.datetime.today().month)}{self.check_num(datetime.datetime.today().year)}{self.check_num(self.last_item+1)}BD"
        self.last_item += 1
        return order_id


order_id_generator = OrderIdGenerator()

