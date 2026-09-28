#estoy importando los comandos de discord
#Siempre que haga una importacion de una libreria
#la primera vez siempre la debo instalar en mi pc
#de la siguiente manera
# abrir terminal (ctrl + ñ) / escribir en la termina
#pip install + NOMBRE_LIBRERIA
from discord.ext import commands
#estoy importando la libreria de discord
import discord

#Traerme los comandos por defecto que tiene un bot de discor
intents = discord.Intents.default()
#De esta manera a los comandos por defecto le doy la aprobacion
#de leer eel contenido de los mensaje
intents.message_content = True

#aca creamos nuestro bot, lo primero es asignar un prefijo
#un prefijo es basicamente que un usuario si se quiere comunicar
#con nuestro bot lo primero que debe ir en el mensaje
#es el simbolo del prfeijo o sea '-'
#y adiccionalmente al bot le damos los comandos creados arriba
bot = commands.Bot(command_prefix='-', intents= intents)

#esto es un decorador en python, es basicamente como decir 
#la funcion de abajo tendra algo especial en este caso sera ser
#un evento de un bot que es algo que siempre se ejecutara
@bot.event
#esto es una funcion asincronica o sea que se ejecuta en el momento
#es decir que le decimos a discord dame tiempo ya te respondo
async def en_linea():

    #esto f string y es la forma profesional de concatenar / unir
    #cadenas de texto con variables
    print (f'Tu bot {bot.user} esta en linea')
    

#esto es un decorador, pero es un command a diferencia del event
#el command espera al llamado que le haga el usuario
#para usarse coloca el prefijo '-' + NOMBRE_FUNCION o sea en discord colocar
#-hola      -> De esta manera es como llamamos al command
@bot.command()
#ctx es basicamente lo que mande el usuario se va a enviar como un
#paquete llamado ctx, es como para recibir la informacion junto
async def hola (ctx):

    #await es como decir esperame discord, ya te envio la respuesta 
    #no te caigas, dame tiempo
    #ctx.send es = a aca esta tu respuesta crack
    #le enviamos la respuesta entre comillas
    await ctx.send('Hola panita :D')

@bot.command()
#el '*' significa que el usuario puede mandar en el mensaje 
# x cantidad o sea puede mandar un mensaje super largo e igualmente
#este comando lo va a recibir
#lo que envie el usuario se va a guardar en una variable
#llamada 'mensaje' y esta a su vez sera de tipo str
#str = string que esto es una cadena de texto
async def despedirse (ctx, *, mensaje:str):

    #lo que envie el usuario lo pasare todo a minuscula con el .lower
    #al igual que le quitare los espacios en blanco con el .strip
    mensaje = mensaje.lower().strip()

    #mediante un condicional iteramos en el mensaje
    #por eso colocamos 'in' de esta manera recorremos el mensaje
    #y si encuentra una coincidencia pues le enviamos
    #su respectiva respuesta
    #si le hubieramos colocado un == solo compararia las
    #primeras lineas
    if 'chao' in mensaje:

        await ctx.send('Chao pescado')

    elif 'vemos' in mensaje:

        await ctx.send('Bueno, este peluche se va pa su estuche')

    else:

        await ctx.send('se me cuida manito')

#el token es la llave del bot y se coloca entre comillas 
#el token lo conseguimos en el portal de desarrolladores de discord
token = ''

#esta linea siempre debe ser la ultima ya que le decimos que todo
#lo que este arriba sera parte del bot y que de una inicie el bot
bot.run(token)