{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "77d39518-0f9b-471d-8ed9-780e12f8c886",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\Users\\pc\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\scipy\\__init__.py:169: UserWarning: A NumPy version >=1.18.5 and <1.26.0 is required for this version of SciPy (detected version 1.26.2\n",
      "  warnings.warn(f\"A NumPy version >={np_minversion} and <{np_maxversion}\"\n"
     ]
    }
   ],
   "source": [
    "#Importamos todas las librerias necesarias\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8504965f-a74d-4716-bbf7-2bfcdee0be40",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Year</th>\n",
       "      <th>Date</th>\n",
       "      <th>Day_of_Week</th>\n",
       "      <th>Hour</th>\n",
       "      <th>Mes</th>\n",
       "      <th>Estacion</th>\n",
       "      <th>Accident_Severity</th>\n",
       "      <th>Number_of_Vehicles</th>\n",
       "      <th>Number_of_Casualties</th>\n",
       "      <th>Road_Type</th>\n",
       "      <th>Speed_limit</th>\n",
       "      <th>Junction_Control</th>\n",
       "      <th>Pedestrian_Crossing-Human_Control</th>\n",
       "      <th>Pedestrian_Crossing-Physical_Facilities</th>\n",
       "      <th>Light_Conditions</th>\n",
       "      <th>Weather_Conditions</th>\n",
       "      <th>Road_Surface_Conditions</th>\n",
       "      <th>Special_Conditions_at_Site</th>\n",
       "      <th>Carriageway_Hazards</th>\n",
       "      <th>Did_Police_Officer_Attend_Scene_of_Accident</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2005</td>\n",
       "      <td>04/01/2005</td>\n",
       "      <td>3</td>\n",
       "      <td>17.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Single carriageway</td>\n",
       "      <td>48.2802</td>\n",
       "      <td>NaN</td>\n",
       "      <td>None within 50 metres</td>\n",
       "      <td>Zebra crossing</td>\n",
       "      <td>Daylight: Street light present</td>\n",
       "      <td>Raining without high winds</td>\n",
       "      <td>Wet/Damp</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2005</td>\n",
       "      <td>05/01/2005</td>\n",
       "      <td>4</td>\n",
       "      <td>17.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Dual carriageway</td>\n",
       "      <td>48.2802</td>\n",
       "      <td>Automatic traffic signal</td>\n",
       "      <td>None within 50 metres</td>\n",
       "      <td>Pedestrian phase at traffic signal junction</td>\n",
       "      <td>Darkness: Street lights present and lit</td>\n",
       "      <td>Fine without high winds</td>\n",
       "      <td>Dry</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2005</td>\n",
       "      <td>06/01/2005</td>\n",
       "      <td>5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>Single carriageway</td>\n",
       "      <td>48.2802</td>\n",
       "      <td>NaN</td>\n",
       "      <td>None within 50 metres</td>\n",
       "      <td>No physical crossing within 50 meters</td>\n",
       "      <td>Darkness: Street lights present and lit</td>\n",
       "      <td>Fine without high winds</td>\n",
       "      <td>Dry</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2005</td>\n",
       "      <td>07/01/2005</td>\n",
       "      <td>6</td>\n",
       "      <td>10.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Single carriageway</td>\n",
       "      <td>48.2802</td>\n",
       "      <td>NaN</td>\n",
       "      <td>None within 50 metres</td>\n",
       "      <td>No physical crossing within 50 meters</td>\n",
       "      <td>Daylight: Street light present</td>\n",
       "      <td>Fine without high winds</td>\n",
       "      <td>Dry</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2005</td>\n",
       "      <td>10/01/2005</td>\n",
       "      <td>2</td>\n",
       "      <td>21.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Single carriageway</td>\n",
       "      <td>48.2802</td>\n",
       "      <td>NaN</td>\n",
       "      <td>None within 50 metres</td>\n",
       "      <td>No physical crossing within 50 meters</td>\n",
       "      <td>Darkness: Street lighting unknown</td>\n",
       "      <td>Fine without high winds</td>\n",
       "      <td>Wet/Damp</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2005</td>\n",
       "      <td>11/01/2005</td>\n",
       "      <td>3</td>\n",
       "      <td>12.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>Single carriageway</td>\n",
       "      <td>48.2802</td>\n",
       "      <td>NaN</td>\n",
       "      <td>None within 50 metres</td>\n",
       "      <td>No physical crossing within 50 meters</td>\n",
       "      <td>Daylight: Street light present</td>\n",
       "      <td>Raining without high winds</td>\n",
       "      <td>Wet/Damp</td>\n",
       "      <td>Ol or diesel</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>2005</td>\n",
       "      <td>13/01/2005</td>\n",
       "      <td>5</td>\n",
       "      <td>20.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>Single carriageway</td>\n",
       "      <td>48.2802</td>\n",
       "      <td>Giveway or uncontrolled</td>\n",
       "      <td>None within 50 metres</td>\n",
       "      <td>No physical crossing within 50 meters</td>\n",
       "      <td>Darkness: Street lights present and lit</td>\n",
       "      <td>Fine without high winds</td>\n",
       "      <td>Dry</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>2005</td>\n",
       "      <td>14/01/2005</td>\n",
       "      <td>6</td>\n",
       "      <td>17.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>Dual carriageway</td>\n",
       "      <td>48.2802</td>\n",
       "      <td>NaN</td>\n",
       "      <td>None within 50 metres</td>\n",
       "      <td>No physical crossing within 50 meters</td>\n",
       "      <td>Daylight: Street light present</td>\n",
       "      <td>Fine without high winds</td>\n",
       "      <td>Dry</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2005</td>\n",
       "      <td>15/01/2005</td>\n",
       "      <td>7</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>Single carriageway</td>\n",
       "      <td>48.2802</td>\n",
       "      <td>Automatic traffic signal</td>\n",
       "      <td>None within 50 metres</td>\n",
       "      <td>Pedestrian phase at traffic signal junction</td>\n",
       "      <td>Darkness: Street lights present and lit</td>\n",
       "      <td>Fine without high winds</td>\n",
       "      <td>Dry</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2005</td>\n",
       "      <td>15/01/2005</td>\n",
       "      <td>7</td>\n",
       "      <td>16.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>Single carriageway</td>\n",
       "      <td>48.2802</td>\n",
       "      <td>Giveway or uncontrolled</td>\n",
       "      <td>None within 50 metres</td>\n",
       "      <td>Central refuge</td>\n",
       "      <td>Daylight: Street light present</td>\n",
       "      <td>Fine without high winds</td>\n",
       "      <td>Dry</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Year        Date  Day_of_Week  Hour  Mes  Estacion  Accident_Severity  \\\n",
       "0  2005  04/01/2005            3  17.0    1         1                  2   \n",
       "1  2005  05/01/2005            4  17.0    1         1                  3   \n",
       "2  2005  06/01/2005            5   0.0    1         1                  3   \n",
       "3  2005  07/01/2005            6  10.0    1         1                  3   \n",
       "4  2005  10/01/2005            2  21.0    1         1                  3   \n",
       "5  2005  11/01/2005            3  12.0    1         1                  3   \n",
       "6  2005  13/01/2005            5  20.0    1         1                  3   \n",
       "7  2005  14/01/2005            6  17.0    1         1                  3   \n",
       "8  2005  15/01/2005            7  22.0    1         1                  3   \n",
       "9  2005  15/01/2005            7  16.0    1         1                  3   \n",
       "\n",
       "   Number_of_Vehicles  Number_of_Casualties           Road_Type  Speed_limit  \\\n",
       "0                   1                     1  Single carriageway      48.2802   \n",
       "1                   1                     1    Dual carriageway      48.2802   \n",
       "2                   2                     1  Single carriageway      48.2802   \n",
       "3                   1                     1  Single carriageway      48.2802   \n",
       "4                   1                     1  Single carriageway      48.2802   \n",
       "5                   2                     1  Single carriageway      48.2802   \n",
       "6                   2                     1  Single carriageway      48.2802   \n",
       "7                   1                     2    Dual carriageway      48.2802   \n",
       "8                   2                     2  Single carriageway      48.2802   \n",
       "9                   2                     5  Single carriageway      48.2802   \n",
       "\n",
       "           Junction_Control Pedestrian_Crossing-Human_Control  \\\n",
       "0                       NaN             None within 50 metres   \n",
       "1  Automatic traffic signal             None within 50 metres   \n",
       "2                       NaN             None within 50 metres   \n",
       "3                       NaN             None within 50 metres   \n",
       "4                       NaN             None within 50 metres   \n",
       "5                       NaN             None within 50 metres   \n",
       "6   Giveway or uncontrolled             None within 50 metres   \n",
       "7                       NaN             None within 50 metres   \n",
       "8  Automatic traffic signal             None within 50 metres   \n",
       "9   Giveway or uncontrolled             None within 50 metres   \n",
       "\n",
       "       Pedestrian_Crossing-Physical_Facilities  \\\n",
       "0                               Zebra crossing   \n",
       "1  Pedestrian phase at traffic signal junction   \n",
       "2        No physical crossing within 50 meters   \n",
       "3        No physical crossing within 50 meters   \n",
       "4        No physical crossing within 50 meters   \n",
       "5        No physical crossing within 50 meters   \n",
       "6        No physical crossing within 50 meters   \n",
       "7        No physical crossing within 50 meters   \n",
       "8  Pedestrian phase at traffic signal junction   \n",
       "9                               Central refuge   \n",
       "\n",
       "                          Light_Conditions          Weather_Conditions  \\\n",
       "0           Daylight: Street light present  Raining without high winds   \n",
       "1  Darkness: Street lights present and lit     Fine without high winds   \n",
       "2  Darkness: Street lights present and lit     Fine without high winds   \n",
       "3           Daylight: Street light present     Fine without high winds   \n",
       "4        Darkness: Street lighting unknown     Fine without high winds   \n",
       "5           Daylight: Street light present  Raining without high winds   \n",
       "6  Darkness: Street lights present and lit     Fine without high winds   \n",
       "7           Daylight: Street light present     Fine without high winds   \n",
       "8  Darkness: Street lights present and lit     Fine without high winds   \n",
       "9           Daylight: Street light present     Fine without high winds   \n",
       "\n",
       "  Road_Surface_Conditions Special_Conditions_at_Site Carriageway_Hazards  \\\n",
       "0                Wet/Damp                        NaN                 NaN   \n",
       "1                     Dry                        NaN                 NaN   \n",
       "2                     Dry                        NaN                 NaN   \n",
       "3                     Dry                        NaN                 NaN   \n",
       "4                Wet/Damp                        NaN                 NaN   \n",
       "5                Wet/Damp               Ol or diesel                 NaN   \n",
       "6                     Dry                        NaN                 NaN   \n",
       "7                     Dry                        NaN                 NaN   \n",
       "8                     Dry                        NaN                 NaN   \n",
       "9                     Dry                        NaN                 NaN   \n",
       "\n",
       "  Did_Police_Officer_Attend_Scene_of_Accident  \n",
       "0                                         Yes  \n",
       "1                                         Yes  \n",
       "2                                         Yes  \n",
       "3                                         Yes  \n",
       "4                                         Yes  \n",
       "5                                         Yes  \n",
       "6                                         Yes  \n",
       "7                                         Yes  \n",
       "8                                         Yes  \n",
       "9                                         Yes  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Leemos nuestro dataframe e imprimimos para tener una primera toma de contacto\n",
    "df = pd.read_csv('Accidents.csv')\n",
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1252f930-8a7e-4311-985d-9541ee2469c1",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1504150, 20)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff4a6a2a-2abc-42b9-a681-a21b1a3ef135",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "c32c3d2d-f5cf-482e-8a3b-dedbb9bc671f",
   "metadata": {},
   "source": [
    "## Creamos las categóricas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "26748a1d-d1bf-4a94-bdaa-025cee7d42b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "lista_cat = ['Special_Conditions_at_Site', 'Pedestrian_Crossing-Physical_Facilities','Light_Conditions',\n",
    "             'Junction_Control','Road_Type','Carriageway_Hazards','Road_Surface_Conditions',\n",
    "             'Pedestrian_Crossing-Human_Control', 'Weather_Conditions', 'Did_Police_Officer_Attend_Scene_of_Accident']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c37a0bb7-a229-4984-81e8-2a6a44b376a2",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "df[lista_cat] = df[lista_cat].astype('category')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "707995d2-a582-4928-9e92-488d0cc557ac",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Year                                              int64\n",
       "Date                                             object\n",
       "Day_of_Week                                       int64\n",
       "Hour                                            float64\n",
       "Mes                                               int64\n",
       "Estacion                                          int64\n",
       "Accident_Severity                                 int64\n",
       "Number_of_Vehicles                                int64\n",
       "Number_of_Casualties                              int64\n",
       "Road_Type                                      category\n",
       "Speed_limit                                     float64\n",
       "Junction_Control                               category\n",
       "Pedestrian_Crossing-Human_Control              category\n",
       "Pedestrian_Crossing-Physical_Facilities        category\n",
       "Light_Conditions                               category\n",
       "Weather_Conditions                             category\n",
       "Road_Surface_Conditions                        category\n",
       "Special_Conditions_at_Site                     category\n",
       "Carriageway_Hazards                            category\n",
       "Did_Police_Officer_Attend_Scene_of_Accident    category\n",
       "dtype: object"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "cc20d946-c568-43e0-988a-dce210b42c52",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('Accidents_categoricas.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de4ba20a-9a0b-4b00-9d62-090e8afd0f52",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "83373b8b-0ad9-4ab8-84cc-7d1437bb1a4c",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "df_corr = df.drop(['Date', 'Special_Conditions_at_Site', 'Pedestrian_Crossing-Physical_Facilities','Light_Conditions',\n",
    "             'Junction_Control','Road_Type','Carriageway_Hazards','Road_Surface_Conditions',\n",
    "             'Pedestrian_Crossing-Human_Control', 'Weather_Conditions', 'Did_Police_Officer_Attend_Scene_of_Accident'], axis=1)\n",
    "correlation_matrix = df_corr.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c27cd6a5-5b72-48dc-9440-bd97e19e9811",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb21c5c1-47e6-4fb3-bce4-3dcd8866a29c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "8b3967a8-95ef-4778-bc8d-cbf7d9c71bfc",
   "metadata": {},
   "source": [
    "# Leyenda\n",
    "- 'Year': año del accidente.\n",
    "- 'Date': fecha del accidente.\n",
    "- 'Day_of_week': día de la semana. 1 es domingo, 2 lunes, etc.\n",
    "- 'Hour': hora, sin minutos ni segundos\n",
    "- 'Estacion': estación del año. 1 invierno, 2 primavera, 3 verano, 4 otoño\n",
    "- 'Accident_Severity': grado de severidad del accidente, va del 1 (+ grave) al 3 (- grave).\n",
    "- 'Number_of_Vehicles': número de vehículos implicados en el accidente.\n",
    "- 'Number_of_Casualties': número de fallecidos en el accidente.\n",
    "- 'Road_Type': tipo de carretera en el cual ocurrió el accidente.\n",
    "- 'Speed_limit': límite de velocidad de la vía en la que se produjo el accidente, en km/h (valores raros y con decimales ya que originalmente está en millas/h)\n",
    "- 'Junction_Control': existencia de controles en los cruces. En el caso de NaN es que no se tienen registros, no que necesariamente esté incontrolada\n",
    "- 'Pedestrian_Crossing-Human_Control': se refiere a si el paso de peatones relacionado con el accidente estaba controlado por alguna persona, como un policía de tráfico o algo parecido.\n",
    "- 'Pedestrian_Crossing-Physical_Facilities': situación del lugar del accidente a la hora de cruzar.\n",
    "- 'Light_Conditions': condiciones de luminosidad en el accidente.\n",
    "- 'Weather_Conditions': condiciones climatológicas bajo las que se ha producido el accidente..\n",
    "- 'Road_Surface_Conditions': condiciones de la vía en que ha ocurrido el accidente.\n",
    "- 'Special_Conditions_at_Site': condiciones especiales del accidente, si las hay.\n",
    "- 'Carriageway_Hazards': existencia de peligros en la carretera en el momento del incidente.\n",
    "- 'Did_Police_Officer_Attend_Scene_of_Accident': hace referencia a si los policias asistieron al lugar del accidente. Sí/no.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e47e2f6b-529b-4135-923d-ab71c975d167",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "47627dea-7581-4999-a306-dd35d0c2d69b",
   "metadata": {},
   "source": [
    "### COLUMNAS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "fb9e1b15-30da-437c-8c7d-fb3104a30e40",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Special_Conditions_at_Site\n",
       "Roadworks                                          17223\n",
       "Ol or diesel                                        5243\n",
       "Mud                                                 4610\n",
       "Road surface defective                              3664\n",
       "Auto traffic singal out                             2788\n",
       "Permanent sign or marking defective or obscured     2269\n",
       "Auto traffic signal partly defective                 785\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Special_Conditions_at_Site\"].value_counts()\n",
    "\n",
    "# CATEGÓRICAS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "e20736ad-437f-476a-9f8f-31556e151cdb",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pedestrian_Crossing-Physical_Facilities\n",
       "No physical crossing within 50 meters          1252571\n",
       "Pedestrian phase at traffic signal junction     100248\n",
       "non-junction pedestrian crossing                 79231\n",
       "Zebra crossing                                   40106\n",
       "Central refuge                                   27660\n",
       "Footbridge or subway                              4300\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Pedestrian_Crossing-Physical_Facilities\"].value_counts()\n",
    "\n",
    "#CATEGÓRICA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d5c6476e-4296-46eb-b244-dc0c070ee576",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Light_Conditions\n",
       "Daylight: Street light present               1102222\n",
       "Darkness: Street lights present and lit       296340\n",
       "Darkeness: No street lighting                  82559\n",
       "Darkness: Street lighting unknown              16120\n",
       "Darkness: Street lights present but unlit       6909\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Light_Conditions\"].value_counts()\n",
    "\n",
    "# CATEGÓRICA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "6706734b-cb00-468e-92df-508d0b909a1c",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Junction_Control\n",
       "Giveway or uncontrolled     733940\n",
       "Automatic traffic signal    155717\n",
       "Stop Sign                     9179\n",
       "Authorised person             2479\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Junction_Control'].value_counts()\n",
    "\n",
    "# CATEGÓRICA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "48e47014-93f9-4890-be68-172fd5d9e286",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Carriageway_Hazards\n",
       "Other object in carriageway                11762\n",
       "Any animal (except a ridden horse)          8014\n",
       "Pedestrian in carriageway (not injured)     3586\n",
       "Involvement with previous accident          2282\n",
       "Dislodged vehicle load in carriageway       1606\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Carriageway_Hazards'].value_counts() \n",
    "\n",
    "# CATEGÓRICA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1d8eb9a9-dbca-479c-9a68-ab2c4ca42d72",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Road_Type\n",
       "Single carriageway    1126951\n",
       "Dual carriageway       221741\n",
       "Roundabout             100463\n",
       "One way street          30981\n",
       "Slip road               15668\n",
       "Unknown                  8346\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Road_Type'].value_counts()\n",
    "\n",
    "# CATEGÓRICA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "92794c2f-85b7-4c00-baa6-ee5b9f1bf60e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pedestrian_Crossing-Human_Control\n",
       "None within 50 metres                 1495269\n",
       "Control by other authorised person       5220\n",
       "Control by school crossing patrol        3644\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Pedestrian_Crossing-Human_Control'].value_counts()\n",
    "\n",
    "# CATEGÓRICA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "91d22cb1-dbeb-4702-b371-4c2a36ae74d9",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Road_Surface_Conditions\n",
       "Dry                          1036628\n",
       "Wet/Damp                      423477\n",
       "Frost/Ice                      31405\n",
       "Snow                           10497\n",
       "Flood (Over 3cm of water)       2143\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Road_Surface_Conditions'].value_counts()\n",
    "\n",
    "# CATEGÓRICA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d8377d94-2ddc-4d97-9c59-edfc59c572bc",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Weather_Conditions\n",
       "Fine without high winds       1203943\n",
       "Raining without high winds     177663\n",
       "Other                           61925\n",
       "Raining with high winds         20813\n",
       "Fine with high winds            18355\n",
       "Snowing without high winds      11301\n",
       "Fog or mist                      8190\n",
       "Snowing with high winds          1960\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Weather_Conditions'].value_counts()\n",
    "\n",
    "# CATEGÓRICAS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ec1572a-c85d-438d-9f2a-965350d0b4b2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
