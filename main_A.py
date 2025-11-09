from ZooA import ZooA
import ZooSubclassA


z1 = ZooA(5, 'Male', 'lion', '21-JUL-2020', 'Golden', 190, 'Nairobi Zoo', 'Savannah', 'Simba')
z2 = ZooA(2, 'Female', 'hyena', '21-JAN-2023', 'Spotted', 60, 'Wildlife Rescue', 'Grasslands', 'Shenzi')


h1 = ZooSubclassA.Hyena(age=4, sex="Male", species="hyena", date_birth="21-JUL-2021",
                          color="Brown", weight=120, came_from="Africa Reserve",
                          habitat="Savannah", name="Shami")

l1 = ZooSubclassA.Lion(age=6, sex="Female", species="lion", date_birth="21-APR-2019",
              color="Golden", weight=280, came_from="Kenya Reserve",
              habitat="Grassland", name="Nala")

t1 = ZooSubclassA.Tiger(age=5, sex="Male", species="tiger", date_birth="21-NOV-2020",
               color="Orange", weight=310, came_from="India Reserve",
               habitat="Jungle", name="Rajah")

b1 = ZooSubclassA.Bear(age=7, sex="Female", species="bear", date_birth="21-JAN-2018",
              color="Brown", weight=400, came_from="Alaska Sanctuary",
              habitat="Forest", name="Baloo")
print(z1)
print(z2)
print(h1.hyena_sounds())
print(l1.lion_sounds())
print(t1.tiger_sounds())
print(b1.bear_sounds())


