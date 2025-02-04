import pandas as pd
import geopandas as gpd
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import math 
import heapq  
from random import *

def clasificacion(osm):
    osm = osm.dropna(subset=['other_tags'])
    cromosomas = {}
    for index, row in osm.iterrows():
        if row.geometry and row.geometry.is_valid:
            coords = row.geometry.coords[0] 
            posicion = (coords[1], coords[0]) 
        else:
            continue

        if '"amenity"=>"fast_food"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 3
        elif '"shop"=>"gas"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"tourism"=>"hotel"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 2
        elif '"amenity"=>"place_of_worship"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 2
        elif '"amenity"=>"school"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 5
        elif '"healthcare"=>"birthing_centre"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 3
        elif '"shop"=>"supermarket"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 4
        elif '"amenity"=>"post_box"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"amenity"=>"pharmacy"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 2
        elif '"amenity"=>"university"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 8
        elif '"amenity"=>"pub"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 2
        elif '"amenity"=>"restaurant"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 3
        elif '"amenity"=>"cinema"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 3
        elif '"shop"=>"convenience"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 2
        elif '"amenity"=>"parking"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"amenity"=>"hospital"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 5
        elif '"leisure"=>"playground"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"amenity"=>"bar"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 2
        elif '"office"=>"government"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 4
        elif '"amenity"=>"bank"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 3
        elif '"amenity"=>"cafe"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 2
        elif '"amenity"=>"fuel"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"gift"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"historic"=>"monument"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"amenity"=>"kindergarten"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"government"=>"healthcare"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 3
        elif '"building"=>"church"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 2
        elif '"amenity"=>"adn"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"amenity"=>"clinic"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 4
        elif '"shop"=>"bakery"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"amenitry"=>"theatre"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 2
        elif '"shop"=>"greengrocer"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"books"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"pastry"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"amenity"=>"ice_cream"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"amenity"=>"pub"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"office"=>"company"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 3
        elif '"office"=>"financial"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 3
        elif '"shop"=>"department_store"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 4
        elif '"amenity"=>"childcare"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"amenity"=>"doctors"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 4
        elif '"shop"=>"florist"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"mobile_phone"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 3
        elif '"leisure"=>"fitness_centre"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 2
        elif '"shop"=>"beuty"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"office"=>"notary"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"videogames"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"amenity"=>"dentist"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"amenity"=>"conference_centre"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 3
        elif '"amenity"=>"events_venue"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 2
        elif '"amenity"=>"college"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 5
        elif '"amenity"=>"police"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 2
        elif '"shop"=>"car"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 3
        elif '"shop"=>"wine"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"laundry"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"motorcicle"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"fashion"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 2
        elif '"shop"=>"electronics"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"beverage"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"car_repair"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 2
        elif '"shop"=>"boutique"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"hairdresser"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"jewerly"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"kiosk"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"hardware"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"toys"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"alcohol"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"tyres"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"pawnbroker"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"wholesale"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 3
        elif '"shop"=>"car_parts"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"mall"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 10
        elif '"shop"=>"chocolate"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"clothes"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"houseware"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 2
        elif '"shop"=>"money_lander"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"motorcicle_repair"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"tool_hire"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"yes"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"electrical"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"shoes"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"fabric"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 5
        elif '"shop"=>"seafood"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1
        elif '"shop"=>"sports"' in row['other_tags']:
            cromosomas[posicion] = cromosomas.get(posicion, 0) + 1




    return cromosomas

def Grafos(gdf_edges,nodos):

    gdf_edges['maxspeed'] = gdf_edges['maxspeed'].fillna(40)
    G = nx.Graph()

    for idx,row in nodos.iterrows():
        x=row['x']
        y=row['y']
        G.add_node(idx,pos=(x, y))

    for idx, row in gdf_edges.iterrows():
        line = row['geometry'] 
        if line.geom_type == 'LineString':
            coords = list(line.coords)
            for i in range(len(coords) - 1):
                start, end = tuple(coords[i]), tuple(coords[i + 1])
                G.add_edge(start, end, weight=math.dist(start,end), geometry=line)
    return G

def Dijkstra(G, start, goal):
    
    distancias = {node: float('inf') for node in G.nodes}
    distancias[start] = 0  

    predecesores = {node: None for node in G.nodes}

    nodos_no_visitados = list(G.nodes)

    while nodos_no_visitados:

        nodo_actual = min(nodos_no_visitados, key=lambda node: distancias[node])

        if nodo_actual == goal:
            break

        nodos_no_visitados.remove(nodo_actual)

        for vecino in G.neighbors(nodo_actual):
            peso = G[nodo_actual][vecino].get("weight", float("inf")) 
            nueva_distancia = distancias[nodo_actual] + peso  

            if nueva_distancia < distancias[vecino]:  
                distancias[vecino] = nueva_distancia  
                predecesores[vecino] = nodo_actual  

    ruta_mas_corta = []
    nodo_actual = goal
    while nodo_actual is not None:
        ruta_mas_corta.append(nodo_actual)
        nodo_actual = predecesores[nodo_actual]
    ruta_mas_corta.reverse()  

    return distancias, ruta_mas_corta

def RanGen(G):
    Nodos = {}
    Nodosnew = {}

    for i in range(30):
        Nodos[i] = {
            "coordx": uniform(-101.05, -100.85),
            "coordy": uniform(22.10, 22.25),
            "pop": randint(100, 3000)
        }

    for i in range(30):
        coord_x = Nodos[i]["coordx"]
        coord_y = Nodos[i]["coordy"]
        
        nearest_node = ox.nearest_nodes(G, coord_x, coord_y)

        Nodosnew[i] = {
            "nearest_node": nearest_node,
            "pop": Nodos[i]["pop"],
            "coordx": coord_x,
            "coordy": coord_y
        }
    
    return Nodosnew 

class DNA():
    def __init__(self, target, mutationrate, n_individuals, n_selection, n_generations):
        self.target = target
        self.mutationrate = mutationrate
        self.n_individuals = n_individuals
        self.n_selection = n_selection
        self.n_generations = n_generations

    def individual(self, min=0, max=29):
        return [randint(min, max) for _ in range(15)]

    def population(self):
        return [self.individual() for _ in range(self.n_individuals)]

    def fitnes(self, individual):
        fitnes = 0
        for i in individual:
            fitnes += Newnodos[i]["pop"]
        return fitnes

    def selection(self, population):
        scores = [(self.fitnes(i), i) for i in population]
        scores = [i[1] for i in sorted(scores)]
        return scores[-self.n_selection:]

    def reproduction(self, population, selected):
        for i in range(len(population)):
            point = randint(1, len(self.individual()) - 1)
            father = sample(selected, 2)
            population[i][:point] = father[0][:point]
            population[i][point:] = father[1][point:]
        return population

    def mutation(self, population):
        for i in range(len(population)):
            if random() <= self.mutationrate:
                point = randint(1, len(self.individual()) - 1)
                newvalue = randint(0, 29)
                while newvalue == population[i][point]:
                    newvalue = randint(0, 29)
                population[i][point] = newvalue
        return population

    def rungenetic(self):
        population = self.population()
        for i in range(self.n_generations):
            print('------------')
            print('Generacion:', i)
            print('Población:', population)
            selected = self.selection(population)
            print('Seleccionados:', selected)
            population = self.reproduction(population, selected)
            population = self.mutation(population)
            best_individual = max(population, key=lambda x: self.fitnes(x))
            best_fitness = self.fitnes(best_individual)
            print('Mejor individuo:', best_individual, 'Fitness:', best_fitness)
            print('Porcentaje de la población total:', (best_fitness / totalpop) * 100, '%')

usable_highways = [
    'motorway', 'trunk', 'primary', 'secondary', 'tertiary',
    'unclassified', 'residential', 'service', 'motorway_link',
    'trunk_link', 'primary_link', 'secondary_link', 'tertiary_link'
]

osm_path = "/home/brandon-aguilera/Escritorio/Modelo/SanLuis.osm"
graph = ox.graph.graph_from_xml(
    osm_path,
    bidirectional=True,
    simplify=True,
    retain_all=True
)

edges_to_keep = []
for u, v, key, data in graph.edges(keys=True, data=True):
    if 'highway' in data and data['highway'] in usable_highways:
        edges_to_keep.append((u, v, key))

graph = graph.edge_subgraph(edges_to_keep)
gdf_nodos, gdf_edges = ox.graph_to_gdfs(graph, nodes=True, edges=True)

Newnodos = RanGen(graph)
totalpop = 0

for i in range(len(Newnodos)):
    totalpop += Newnodos[i]["pop"]


target = totalpop * 0.6
model = DNA(target=target, mutationrate=0.02, n_individuals=20, n_selection=5, n_generations=50)
model.rungenetic()
print(totalpop)