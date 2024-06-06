import time
from obb import DataExtract

computrabajo = DataExtract("https://co.computrabajo.com/")
computrabajo.ingresar_link()
computrabajo.busqueda_xpath("/html/body/main/div[2]/div/div/div/div[1]/div/div[1]/form/input[1]").send_keys("Informatica")
computrabajo.busqueda_xpath("/html/body/main/div[2]/div/div/div/div[1]/div/div[2]/form/input[1]").send_keys("Colombia")
computrabajo.busqueda_xpath("/html/body/main/div[2]/div/div/div/div[1]/button").click() # buscar
time.sleep(1)
computrabajo.busqueda_xpath("/html/body/main/div[2]/div[2]/div/button[1]").click() # Banner
time.sleep(1)
computrabajo.obtener_perfiles_paginados('js-o-link',3,'//*[@id="offersGridOfferContainer"]/div[8]/span[2]')
computrabajo.Cerrar_drive()
json = computrabajo.Guardar_perfiles_paginados()
print(json)