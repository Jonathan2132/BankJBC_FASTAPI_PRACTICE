import psycopg2 as p2

conection = {
    "host":"c67okggoj39697.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com",
    "port":5432,
    "user":"ud6l5k37ghktp8",
    "password":"p242fd8e1711b81a16d19e10b03e41288cad67cbee81c46fd024ed4dcdcf1a840",
    "database":"dh6o98h2fog95"


}

try:
    conection = p2.connect(**conection)
    if conection:
        print("Estas conectado ala base de datos")
        

except:
    print("NO fue posible conectarse")


