class VendingMachineDFA:
    def __init__(self, filename):
        self.states = []
        self.alphabet = []
        self.start_state = ""
        self.accept_states = []
        self.transitions = {}
        self.current_state = ""
        self.trajectory = []
        self.drink_prices = {"A": 3000, "B": 4000, "C": 6000}
        self.max_input = 10000
        
        self.parse_dfa_file(filename)
        self.current_state = self.start_state
        self.trajectory = [self.current_state]
    
    def parse_dfa_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                
                for line in lines:
                    line = line.strip()
                    if line.startswith("States:"):
                        self.states = [state.strip() for state in line[7:].split(',')]
                    elif line.startswith("Alphabet:"):
                        self.alphabet = [symbol.strip() for symbol in line[9:].split(',')]
                    elif line.startswith("Start:"):
                        self.start_state = line[6:].strip()
                    elif line.startswith("Accept:"):
                        self.accept_states = [state.strip() for state in line[7:].split(',')]
                    elif line.startswith("Transitions:"):
                        continue
                    elif len(line.split()) == 3:
                        from_state, symbol, to_state = line.split()
                        if from_state not in self.transitions:
                            self.transitions[from_state] = {}
                        self.transitions[from_state][symbol] = to_state
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
            exit(1)
    
    def get_next_state(self, current_state, input_symbol):
        if current_state in self.transitions and input_symbol in self.transitions[current_state]:
            return self.transitions[current_state][input_symbol]
        return None
    
    def process_input(self, input_symbol):
        current_value = int(self.current_state[1:]) if self.current_state != "S0" else 0
        
        if input_symbol in ["A", "B", "C"]:
            price = self.drink_prices[input_symbol]
            if current_value < price:
                return f"Not enough money to buy Drink {input_symbol}. You have {current_value}."
            
            change = current_value - price
            self.current_state = self.start_state
            self.trajectory.append(self.current_state)
            return (f"DFA trajectory: {' -> '.join(self.trajectory)}\n"
                    f"Drink {input_symbol} can be purchased. Status: ACCEPTED.\n"
                    f"Returns: {change}")
        
        try:
            money = int(input_symbol)
            if money not in [1000, 2000, 5000, 10000]:
                return "Invalid money input. Please enter 1000, 2000, 5000, or 10000."
            
            new_value = current_value + money
            if new_value > self.max_input:
                return f"Error: If you enter {money}, the value exceeds the limit of {self.max_input}."
            
            next_state = f"S{new_value}"
            if next_state in self.states:
                self.current_state = next_state
                self.trajectory.append(self.current_state)
                
                on_drinks = []
                for drink, price in self.drink_prices.items():
                    if new_value >= price:
                        on_drinks.append(f"Minuman {drink}")
                
                if on_drinks:
                    on_message = "ON: " + ", ".join(on_drinks)
                else:
                    on_message = "Belum ada minuman yang dapat dibeli."
                
                return f"Current money: {new_value}\n{on_message}"
            else:
                return "Invalid state transition."
            
        except ValueError:
            return "Invalid input. Please enter money (1000, 2000, 5000, 10000) or buy a drink (A, B, C)."
    
    def run(self):
        print("Vending Machine DFA Simulator")
        print(f"Starting state: {self.current_state}")
        print("Drink prices: A: 3000, B: 4000, C: 6000")
        print("Maximum input value: 10000")
        
        while True:
            input_symbol = input("\nEnter money or buy a drink (1000, 2000, 5000, 10000, A, B, C): ")
            if input_symbol.lower() == 'exit':
                print("Exiting the simulator...")
                break
                
            result = self.process_input(input_symbol)
            print(result)
            
            
            if "can be purchased" in result:
            
                print("Program selesai karena minuman sudah dibeli.")
                break


def main():
    dfa = VendingMachineDFA("vending_dfa.txt")
    dfa.run()

if __name__ == "__main__":
    main()
