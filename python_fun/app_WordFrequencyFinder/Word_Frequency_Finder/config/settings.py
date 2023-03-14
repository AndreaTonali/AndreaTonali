from environs import Env

env = Env()

TEXT_FILE = env("TEXT_FILE", "./words.txt")
