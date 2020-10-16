from tkinter import *

#creating class
class currencyconverter: 
	def __init__(self):

		#creating a window
		window = Tk()

		#adding a title to the main window
		window.title("Currency Converter")

		#giving bg color to the main window
		window.configure(bg = "grey")

		#labelling widgets to the main window
		Label(window, font = "Helvetica 12 bold", bg = "grey", text = "Amount to convert").grid(row =1,column = 1, sticky = W)
		Label(window, font = "Helvetica 12 bold", bg = "grey", text = "Conversion Rate").grid(row =2,column = 1, sticky = W)
		Label(window, font = "Helvetica 12 bold", bg = "grey", text = "Converted Amount").grid(row =3,column = 1, sticky = W)


		self.AmounttoConvertVar = StringVar()
		Entry(window, textvariable = self.AmounttoConvertVar, justify = RIGHT).grid(row =1, column = 2)
		
		self.ConversionRateVar = StringVar()
		Entry(window, textvariable = self.ConversionRateVar, justify = RIGHT).grid(row = 2, column = 2)
		
		self.ConvertedAmountVar = StringVar()
		ConvertedAmountlbl = Label(window, font ="Helvetica 12 bold", bg="grey", textvariable = self.ConvertedAmountVar).grid(row = 3 , column = 2, sticky=E)

		btConvertedAmount = Button(window, text = "convert", font = "Helvetica 12 bold", bg= "green", fg = "black", command = self.ConvertedAmount).grid(row =4, column=2, sticky=E)
		btdelete_all = Button(window, text = "clear", font = "Helvetica 12 bold", bg = "red", fg = "black", command = self.delete_all).grid(row =4, column = 6, padx= 25, pady = 25, sticky = E)

		window.mainloop()

	def ConvertedAmount(self):
		amount = float(self.ConversionRateVar.get()) 
		ConvertedAmountVar = float(self.AmounttoConvertVar.get()) * amount
		self.ConvertedAmountVar.set(format(ConvertedAmountVar, '10.2f')) 

	def delete_all(self):
		self.AmounttoConvertVar.set("")
		self.ConversionRateVar.set("")
		self.ConvertedAmountVar.set("")

currencyconverter()