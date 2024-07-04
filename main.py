import tkinter as tk
from tkinter import messagebox

class BlackjackCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Card Counter")

        self.deck_count = tk.DoubleVar(value=1)
        self.card_values = {'2': 1, '3': 1, '4': 2, '5': 2, '6': 1, '7': 1,
                            '8': 0, '9': 0, '10': -2, 'J': -2, 'Q': -2, 'K': -2, 'A': 0}
        self.running_count = 0
        self.selected_cards = 0
        self.victories = 0
        self.defeats = 0

        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack()

        # Title Label
        title_label = tk.Label(main_frame, text="Blackjack Card Counter", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Number of Decks Label and Entry
        deck_label = tk.Label(main_frame, text="Número de mazos:")
        deck_label.grid(row=1, column=0, sticky=tk.W)

        self.deck_entry = tk.Entry(main_frame, textvariable=self.deck_count, width=5)
        self.deck_entry.grid(row=1, column=1, sticky=tk.W, pady=10)
        self.deck_count.trace_add("write", self.update_true_count)

        # Card Selection Label
        card_label = tk.Label(main_frame, text="Seleccionar carta:")
        card_label.grid(row=2, column=0, sticky=tk.W)

        # Frame for Card Buttons
        card_buttons_frame = tk.Frame(main_frame)
        card_buttons_frame.grid(row=2, column=1, columnspan=2, sticky=tk.W)

        # Create buttons for each card
        for idx, card in enumerate(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']):
            btn = tk.Button(card_buttons_frame, text=card, width=3, height=1, command=lambda c=card: self.add_card(c))
            btn.grid(row=idx // 4, column=idx % 4, padx=5, pady=5)

        # Reset Button
        reset_button = tk.Button(main_frame, text="Reiniciar", command=self.reset_count)
        reset_button.grid(row=3, column=0, columnspan=3, pady=10)

        # Running Count Label
        self.result_label = tk.Label(main_frame, text="Running Count: 0", font=("Helvetica", 12))
        self.result_label.grid(row=4, column=0, columnspan=3, pady=10)

        # True Count Label
        self.true_count_label = tk.Label(main_frame, text="Conteo verdadero: 0", font=("Helvetica", 12))
        self.true_count_label.grid(row=5, column=0, columnspan=3, pady=10)

        # Selected Cards Label
        self.selected_cards_label = tk.Label(main_frame, text="Cartas seleccionadas total: 0", font=("Helvetica", 12))
        self.selected_cards_label.grid(row=6, column=0, columnspan=3, pady=10)

        # Hand Entry
        hand_label = tk.Label(main_frame, text="Ingrese su mano:")
        hand_label.grid(row=7, column=0, sticky=tk.W)

        self.hand_card1_entry = tk.Entry(main_frame, width=5)
        self.hand_card1_entry.grid(row=7, column=1, sticky=tk.W, pady=10)

        self.hand_card2_entry = tk.Entry(main_frame, width=5)
        self.hand_card2_entry.grid(row=7, column=2, sticky=tk.W, pady=10)

        # Dealer's Card Entry
        dealer_card_label = tk.Label(main_frame, text="Carta del crupier:")
        dealer_card_label.grid(row=8, column=0, sticky=tk.W)

        self.dealer_card_entry = tk.Entry(main_frame, width=5)
        self.dealer_card_entry.grid(row=8, column=1, sticky=tk.W, pady=10)

        # Suggestion Button
        suggest_button = tk.Button(main_frame, text="Sugerir", command=self.suggest_action)
        suggest_button.grid(row=9, column=0, columnspan=3, pady=10)

        # Suggestion Label
        self.suggestion_label = tk.Label(main_frame, text="Sugerencia: ", font=("Helvetica", 12))
        self.suggestion_label.grid(row=10, column=0, columnspan=3, pady=10)

        # Victories Label and Button
        self.victories_label = tk.Label(main_frame, text="Victorias: 0", font=("Helvetica", 12))
        self.victories_label.grid(row=11, column=0, pady=10)
        victory_button = tk.Button(main_frame, text="Victoria", command=self.record_victory)
        victory_button.grid(row=11, column=1, padx=5, pady=10)

        # Defeats Label and Button
        self.defeats_label = tk.Label(main_frame, text="Derrotas: 0", font=("Helvetica", 12))
        self.defeats_label.grid(row=12, column=0, pady=10)
        defeat_button = tk.Button(main_frame, text="Derrota", command=self.record_defeat)
        defeat_button.grid(row=12, column=1, padx=5, pady=10)

        # Global Score Label
        self.global_score_label = tk.Label(main_frame, text="Puntuación global: 0", font=("Helvetica", 12))
        self.global_score_label.grid(row=13, column=0, columnspan=3, pady=10)

    def add_card(self, card):
        if card in self.card_values:
            self.running_count += self.card_values[card]
            self.selected_cards += 1
            self.update_count()
            if self.selected_cards == 52:
                messagebox.showinfo("Deck Alert", "Se han jugado 52 cartas, se acabó un mazo")
                self.selected_cards = 0
        else:
            messagebox.showerror("Invalid Card", "Por favor, ingrese una carta válida (2-10, J, Q, K, A).")

    def update_count(self):
        self.result_label.config(text=f"Running Count: {self.running_count}")
        self.selected_cards_label.config(text=f"Cartas seleccionadas: {self.selected_cards}")
        self.update_true_count()

    def update_true_count(self, *args):
        try:
            true_count = round(self.running_count / float(self.deck_count.get()), 2)
            self.true_count_label.config(text=f"Conteo verdadero: {true_count}")
        except ValueError:
            pass  # Manejar si el número de mazos no es válido

    def reset_count(self):
        self.running_count = 0
        self.selected_cards = 0
        self.victories = 0
        self.defeats = 0
        self.update_count()
        self.deck_count.set(1)
        self.update_global_score()

    def record_victory(self):
        self.victories += 1
        self.victories_label.config(text=f"Victorias: {self.victories}")
        self.update_global_score()

    def record_defeat(self):
        self.defeats += 1
        self.defeats_label.config(text=f"Derrotas: {self.defeats}")
        self.update_global_score()

    def update_global_score(self):
        global_score = self.victories - self.defeats
        self.global_score_label.config(text=f"Puntuación global: {global_score}")

    def suggest_action(self):
        card1 = self.hand_card1_entry.get().strip()
        card2 = self.hand_card2_entry.get().strip()
        dealer_card = self.dealer_card_entry.get().strip()

        if not card1 or not card2 or not dealer_card:
            messagebox.showerror("Mano Inválida", "Por favor, ingrese una mano y la carta del crupier válidas.")
            return

        hand = [card1, card2]
        total = 0
        aces = 0
        for card in hand:
            if card.isdigit():
                total += int(card)
            elif card in ['J', 'Q', 'K']:
                total += 10
            elif card == 'A':
                aces += 1
                total += 11

        # Ajustar por ases
        while total > 21 and aces:
            total -= 10
            aces -= 1

        true_count = self.running_count / self.deck_count.get()

        suggestion = ""
        if len(hand) == 2 and hand[0] == hand[1] and true_count >= 5:
            suggestion = "Dividir"
        elif total >= 17:
            suggestion = "Plantarse"
        elif total >= 13 and true_count >= -1:
            suggestion = "Plantarse"
        elif total == 12 and true_count >= 3:
            suggestion = "Plantarse"
        elif total == 11 and true_count >= 1:
            suggestion = "Doblar"
        elif total == 10 and true_count >= 0:
            suggestion = "Doblar"
        else:
            suggestion = "Pedir carta"

        self.suggestion_label.config(text=f"Sugerencia: {suggestion}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackCounterApp(root)
    root.mainloop()