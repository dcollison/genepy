# External Imports
import math as m
import genepy as gp
from matplotlib import pyplot as plt

# Internal Imports
from organism_implementation import OrganismImpl
from target import Target

# Config
population_size = 500
mutation_rate = 0.2
n_generations = 1000
organism_type = OrganismImpl
target = Target(0, 90)
elitism = 4
# Setup
ga = gp.genetic_algorithm.GeneticAlgorithm(organism_type,
                                           target,
                                           population_size,
                                           mutation_rate,
                                           n_generations,
                                           elitism)

# Visualisation
f = plt.figure()
ax = plt.axes()
plt.grid()
plt.axis('scaled')
plt.xlim([-100, 100])
plt.ylim([-100, 100])
ax.add_patch(plt.Circle(xy=target.position, radius=4, color='r'))
ax.add_patch(plt.Rectangle(xy=[-100, -40], width=150, height=5, color='k'))
ax.add_patch(plt.Rectangle(xy=[-20, 20], width=120, height=5, color='k'))
ax.add_patch(plt.Rectangle(xy=[-20, -5], width=5, height=30, color='k'))
ax.add_patch(plt.Rectangle(xy=[-100, 10], width=50, height=5, color='k'))
ax.add_patch(plt.Rectangle(xy=[-100, 60], width=125, height=5, color='k'))

ga.main()

fittest_organism = ga.get_fittest()

print("\n***Best Organism***")
print(fittest_organism[0])
