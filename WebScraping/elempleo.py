import time
from obb import DataExtract

elempleo = DataExtract("https://www.elempleo.com/co/ofertas-empleo")
elempleo.ingresar_link()
elempleo.busqueda_xpath("/html/body/header/div/div[2]/div[2]/div/form/div/span/input[2]").send_keys("informática")
elempleo.busqueda_xpath("/html/body/header/div/div[2]/div[2]/div/form/div/button").click()
elempleo.scroll_down("/html")
elempleo.busqueda_xpath("/html/body/div[8]/div[3]/div[1]/div[4]/div/form/div/select").click() # Buscar
elempleo.busqueda_xpath("/html/body/div[8]/div[3]/div[1]/div[4]/div/form/div/select").click() # 100
elempleo.busqueda_xpath("/html/body/div[8]/div[3]/div[1]/div[4]/div/form/div/select").send_keys("100") # 100
time.sleep(2)
elempleo.Obtener_perfiles("js-offer-title", "info-company-name", "info-city")
elempleo.Cerrar_drive()
data_elempleo = elempleo.Guardar_perfiles()
print(data_elempleo)