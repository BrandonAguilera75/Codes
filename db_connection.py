import mysql.connector
import os 
import numpy as np
import h5py

host = 'localhost'
user = 'newuser'
password = 'newpassword'
port = '3306'
database = 'DataBaseNoMod'

def upload_file(path):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
        print("Conexión exitosa a la base de datos")

        
        with open(path, 'rb') as archivo:
            arch = archivo.read()

            with h5py.File(path,'r') as hf:
             data1=hf.get('data')
             dataset1=np.array(data1)

            wavelen=dataset1[0, :,0] 
            
            cursor_insert1 = connection.cursor()
            
            cursor_insert1.execute("""
                INSERT INTO Archivos (archivo) 
                VALUES (%s)
            """, (arch,))
            if cursor_insert1.rowcount > 0:
                print("Archivo insertado correctamente.")
            else:
                print("No se insertó ningún archivo.")
            
            connection.commit()
            cursor_insert1.close()


            cursor_select1 = connection.cursor(buffered=True)
            cursor_select1.execute("""
                SELECT id_archivo FROM Archivos
                WHERE archivo=%s              
            """, (arch,))
            

            
        
            id_arch  = cursor_select1.fetchone()[0]

            cursor_select1.close()


            cursor = connection.cursor()
            
            for j in range(len(wavelen)):
             avrgw_te=np.mean(dataset1[:,j,5])
             avrgw_tm=np.mean(dataset1[:,j,6])

             stderw_te=np.sqrt(np.var(dataset1[:,j,5]))
             stderw_tm=np.sqrt(np.var(dataset1[:,j,6]))
             wl=wavelen[j]
             cursor.execute("""
                INSERT INTO Resultados (Id_Arch,WaveLen,AvrgW_TE,AvrgW_TM,StarDerW_TE,StarDerW_TM) 
                VALUES (%s,%s,%s,%s,%s,%s)
             """, (id_arch,wl,avrgw_te,avrgw_tm,stderw_te,stderw_tm))
            
            connection.commit()
            cursor.close()


       

    
    finally:
        if connection.is_connected():
            connection.close()
            print("Conexión cerrada")



def get_file(id_archivo):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
        print("Conexión exitosa a la base de datos")
        
        cursor = connection.cursor()
        cursor.execute("""
            SELECT archivo FROM archivos 
            WHERE id_archivo = %s
        """, (id_archivo,))
        
        idstr=str(id_archivo)
        
        resultado = cursor.fetchone()
        
        
        file_path = os.path.join(script_dir, f"data{idstr}.h5")
        
        if resultado is not None:
            with open(file_path, 'wb') as outfile:
                outfile.write(resultado[0])
            print("Archivo recuperado y guardado correctamente.")
        

        else:
            print(f"No se encontró ningún archivo con ese id={id_archivo}")

        #with h5py.File(file_path,'r') as hf:
        #    data1=hf.get('data')
        #    dataset1=np.array(data1)

        cursor.close()
    
    except mysql.connector.Error as e:
        print(f"Error al conectar o ejecutar la consulta: {e}")
    
    finally:
        if connection.is_connected():
            connection.close()
            print("Conexión cerrada")




def get_files(lowlim,uplim):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
        print("Conexión exitosa a la base de datos")
        
        cursor = connection.cursor()
        cursor.execute("""
            SELECT archivo FROM archivos 
            WHERE id_archivo BETWEEN %s AND %s
        """, (lowlim,uplim))
        
        x=lowlim

        for (archivo) in cursor:
         x+=1
         file_path = os.path.join(script_dir, f"data{x}.h5")
         if archivo is not None:
            with open(file_path, 'wb') as outfile:
                outfile.write(archivo)
    
        



    except mysql.connector.Error as e:
        print(f"Error al conectar o ejecutar la consulta: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("Conexión cerrada")



def get_oneavr(id_archivo,wavelen,x):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
        print("Conexión exitosa a la base de datos")
        
        if x == 'TM': 
         cursor = connection.cursor()
         cursor.execute("""
            SELECT AvrgW_TM, StarDerW_TM FROM Resultados 
            WHERE Id_Arch = %s AND WaveLen =%s
         """, (id_archivo,wavelen))
         for avr, stde in cursor:
            print("En el archivo {} con la longitud de onda {} el promedio es {} y la desviacion estandar{}".format(id_archivo,wavelen,avr,stde))
        elif x == 'TE': 
         cursor = connection.cursor()
         cursor.execute("""
            SELECT AvrgW_TE, StarDerW_TE FROM Resultados 
            WHERE iId_Arch = %s AND WaveLen =%s
         """, (id_archivo,wavelen))
         for avr, stde in cursor:
            print("En el archivo {} con la longitud de onda {} el promedio es {} y la desviacion estandar{}".format(id_archivo,wavelen,avr,stde))
        else:
           print("Opcion Invalida")    




    except mysql.connector.Error as e:
        print(f"Error al conectar o ejecutar la consulta: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("Conexión cerrada")

def get_wholeavr(id_archivo,x):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database
        )
        print("Conexión exitosa a la base de datos")
        
        if x == 'TM': 
         cursor = connection.cursor()
         cursor.execute("""
            SELECT AvrgW_TM, StarDerW_TM, WaveLen FROM Resultados 
            WHERE Id_Arch = %s 
         """, (id_archivo,))
         for avr, stde,wavelen in cursor:
            print("En el archivo {} con la longitud de onda {} el promedio es {} y la desviacion estandar{}".format(id_archivo,wavelen,avr,stde))
        elif x == 'TE': 
         cursor = connection.cursor()
         cursor.execute("""
            SELECT AvrgW_TE, StarDerW_TE,WaveLen FROM Resultados 
            WHERE iId_Arch = %s
         """, (id_archivo))
         for avr, stde,wavelen in cursor:
            print("En el archivo {} con la longitud de onda {} el promedio es {} y la desviacion estandar{}".format(id_archivo,wavelen,avr,stde))
        else:
           print("Opcion Invalida")    




    except mysql.connector.Error as e:
        print(f"Error al conectar o ejecutar la consulta: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("Conexión cerrada")


script_dir = os.path.dirname(os.path.abspath(__file__))

get_wholeavr(27,'TM')
#upload_file(path="/home/brandon-aguilera/Escritorio/h5/data0.h5")