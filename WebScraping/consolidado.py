#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:06:49 2023

@author: cscc
"""
import time
import pandas as pd
from obb import DataExtract

# Linkedin
linkedin = DataExtract('https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0')
linkedin.ingresar_link()
linkedin.busqueda_id("job-search-bar-keywords").send_keys('Informatica')
linkedin.busqueda_id("job-search-bar-location").clear()
linkedin.busqueda_id("job-search-bar-location").send_keys('Colombia')
linkedin.busqueda_xpath("//*[@id='jobs-search-panel']/form/button").click()
time.sleep(1)
linkedin.scroll_down_smoothly()
linkedin.obtener_perfiles_final('base-search-card__title') # linkedin.Obtener_perfiles('base-search-card__title','base-search-card__subtitle','job-search-card__location')
data_linkedin=linkedin.guardar_perfiles_final() # data_linkedin=linkedin.Guardar_perfiles()

# El empleo
elempleo = DataExtract("https://www.elempleo.com/co/ofertas-empleo")
elempleo.ingresar_link()
elempleo.busqueda_xpath("/html/body/header/div/div[2]/div[2]/div/form/div/span/input[2]").send_keys("informática")
elempleo.busqueda_xpath("/html/body/header/div/div[2]/div[2]/div/form/div/button").click()
elempleo.scroll_down("/html")
elempleo.busqueda_xpath("/html/body/div[8]/div[3]/div[1]/div[4]/div/form/div/select").click() # Buscar
elempleo.busqueda_xpath("/html/body/div[8]/div[3]/div[1]/div[4]/div/form/div/select").click() # 100
elempleo.busqueda_xpath("/html/body/div[8]/div[3]/div[1]/div[4]/div/form/div/select").send_keys("100") # 100
time.sleep(2)
elempleo.obtener_perfiles_final("js-offer-title") # elempleo.Obtener_perfiles("js-offer-title", "info-company-name", "info-city")
data_elempleo = elempleo.guardar_perfiles_final() # data_elempleo = elempleo.Guardar_perfiles()

# Computrabajo
computrabajo = DataExtract("https://co.computrabajo.com/")
computrabajo.ingresar_link()
computrabajo.busqueda_xpath("/html/body/main/div[2]/div/div/div/div[1]/div/div[1]/form/input[1]").send_keys("Informatica")
computrabajo.busqueda_xpath("/html/body/main/div[2]/div/div/div/div[1]/div/div[2]/form/input[1]").send_keys("Colombia")
time.sleep(2)
computrabajo.click_banner_button("/html/body/div/div[1]/div/div[1]/div[2]/svg/path[1]")
computrabajo.busqueda_xpath("/html/body/main/div[2]/div/div/div/div[1]/button").click() # buscar
time.sleep(2)
computrabajo.click_banner_button("/html/body/main/div[2]/div[2]/div/button[1]")
time.sleep(1)
computrabajo.obtener_perfiles_paginados_final('js-o-link',3,'//*[@id="offersGridOfferContainer"]/div[8]/span[2]')
data_computrabajo = computrabajo.guardar_perfiles_paginados_final()
computrabajo.Cerrar_drive()

data_frames = [data_linkedin, data_elempleo, data_computrabajo]
# Unir los DataFrames en uno solo
df = pd.concat(data_frames, ignore_index=True)
df.to_csv('Resultado.csv', index=False, mode="w") # Guardar como CSV