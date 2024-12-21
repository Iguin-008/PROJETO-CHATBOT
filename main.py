
import mensagem
import telebot
import dotenv
from os import getenv

dotenv.load_dotenv()

TOKEN_TELEGRAM = getenv("TOKEN_TELEGRAM")


bot = telebot.TeleBot(TOKEN_TELEGRAM)

comandos = (
    "/opcao1 - Dispositivos Pessoais",
    "/opcao2 - Eletrodomésticos",
    "/opcao3 - Equipamentos de Escritório",
    "/opcao4 - Acessórios e Baterias"

)

opcao1_comandos = (
    "/subopcao1 - Celulares",
    "/subopcao2 - Tablets",
    "/subopcao3 - Computadores"
)
opcao2_comandos = (
    "/subopcao1_op2 - Geladeira",
    "/subopcao2_op2 - Micro-Ondas",
    "/subopcao3_op2 - Televisores",
    "/subopcao4_op2 - Aspirador de Pó"
)
opcao3_comandos = (
    "/subopcao1_op3 - Impressora",
    "/subopcao2_op3 - Mouse",
    "/subopcao3_op3 - Teclados",
    "/subopcao4_op3 - Monitores"
)
opcao4_comandos = (
    "/subopcao1_op4 - Cabos",
    "/subopcao2_op4 - Carregadores",
    "/subopcao3_op4 - Pilhas e Baterias"
)


@bot.message_handler(commands=["start"])
def mensagem_boas_vindas(message):
    bot.send_message(message.chat.id, mensagem.BOAS_VINDAS) 
    bot.send_message(message.chat.id, comandos[0])
    bot.send_message(message.chat.id, comandos[1])
    bot.send_message(message.chat.id, comandos[2])
    bot.send_message(message.chat.id, comandos[3])

    
@bot.message_handler(commands=["opcao1"])
def opcao1(message):
    bot.send_message(message.chat.id, "Você clicou em Dispositivos Pessoais. Agora escolha uma das subopções:")
    for subcomando in opcao1_comandos:
        bot.send_message(message.chat.id, subcomando)
    
@bot.message_handler(commands=["subopcao1"])
def subopcao1(message):
    bot.send_message(message.chat.id, mensagem.DIS_CELULAR)

@bot.message_handler(commands=["subopcao2"])
def subopcao2(message):
    bot.send_message(message.chat.id, mensagem.DIS_TABLET)
    
@bot.message_handler(commands=["subopcao3"])
def subopcao3(message):
    bot.send_message(message.chat.id, mensagem.DIS_COMPUTADORES)
    


    
@bot.message_handler(commands=["opcao2"])
def opcao2(message):
    bot.send_message(message.chat.id, "Você clicou em Eletrodomésticos. Agora escolha uma das subopções:")
    for subcomando in opcao2_comandos:
        bot.send_message(message.chat.id, subcomando)

@bot.message_handler(commands=["subopcao1_op2"])
def subopcao1(message):
    bot.send_message(message.chat.id, mensagem.DIS_GELADEIRA)

@bot.message_handler(commands=["subopcao2_op2"])
def subopcao2(message):
    bot.send_message(message.chat.id, mensagem.DIS_MICROONDAS)
    
@bot.message_handler(commands=["subopcao3_op2"])
def subopcao3(message):
    bot.send_message(message.chat.id, mensagem.DIS_TELEVISORES)
    
@bot.message_handler(commands=["subopcao4_op2"])
def subopcao4(message):
    bot.send_message(message.chat.id, mensagem.DIS_ASPIRADOR)
        
        
        

@bot.message_handler(commands=["opcao3"])
def opcao3(message):
    bot.send_message(message.chat.id, "Você clicou em Equipamentos de Escritório. Agora escolha uma das subopções:")
    for subcomando in opcao3_comandos:
        bot.send_message(message.chat.id, subcomando)
        
@bot.message_handler(commands=["subopcao1_op3"])
def subopcao1(message):
    bot.send_message(message.chat.id, mensagem.DIS_IMPRESSORA)

@bot.message_handler(commands=["subopcao2_op3"])
def subopcao2(message):
    bot.send_message(message.chat.id, mensagem.DIS_MOUSE)
    
@bot.message_handler(commands=["subopcao3_op3"])
def subopcao3(message):
    bot.send_message(message.chat.id, mensagem.DIS_TECLADOS)
    
@bot.message_handler(commands=["subopcao4_op3"])
def subopcao4(message):
    bot.send_message(message.chat.id, mensagem.DIS_MONITORES)    
    

    
        
@bot.message_handler(commands=["opcao4"])
def opcao4(message):
    bot.send_message(message.chat.id, "Você clicou em Acessórios e Baterias. Agora escolha uma das subopções:")
    for subcomando in opcao4_comandos:
        bot.send_message(message.chat.id, subcomando)
        
@bot.message_handler(commands=["subopcao1_op4"])
def subopcao1(message):
    bot.send_message(message.chat.id, mensagem.DIS_CABOS)

@bot.message_handler(commands=["subopcao2_op4"])
def subopcao2(message):
    bot.send_message(message.chat.id, mensagem.DIS_CARREGADORES)
    
@bot.message_handler(commands=["subopcao3_op4"])
def subopcao3(message):
    bot.send_message(message.chat.id, mensagem.DIS_PILHAS_BATERIAS)
    
        
        
if __name__ == "__main__":
    bot.polling()
    
    
