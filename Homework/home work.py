#1
# def number_generator():
#     for number in range(10):
#         yield number
# for num in number_generator():
#     print(num)
#2
# def even_number_generator(start, end):
#     for number in range(start, end + 1):
#         if number % 2 == 0:
#             yield number
# start = 1
# end = 10
# for even_number in even_number_generator(start, end):
#     print(even_number)
#3
# def string_character_generator(input_string):
#     for char in input_string:
#         yield char
# # Example usage:
# text = "Hello, World!"
# generator = string_character_generator(text)
# for character in generator:
#     print(character)
#4
# def square_generator(N):
#     for i in range(N):
#         yield i * i
# N = 5
# for square in square_generator(N):
#     print(square)
#5
# def juft_sonlar(chegara):
#     for son in range(0, chegara + 1, 2):
#         yield son
# def toq_sonlar(chegara):
#     for son in range(1, chegara + 1, 2):
#         yield son
# juft_gen = juft_sonlar(10)
# toq_gen = toq_sonlar(10)
# print("Juft sonlar:")
# for juft in juft_gen:
#     print(juft)
# print("\nToq sonlar:")
# for toq in toq_gen:
#     print(toq)
