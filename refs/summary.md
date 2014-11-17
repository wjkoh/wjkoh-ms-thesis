# Background Study
Our method can be named view-dependent simulation level-of-detail (VSLOD) or view-dependent multiresolution simulation.

## 1. Simulation
### Category of Simulation level of detail (SLOD)
Methods in this category change a dynamic model from complex one to simple one, for example from a full rigid body model to a point-mass model, to achieve faster simulation speed.

#### Carlson, D.A. and Hodgins, J.K. 1997. Simulation levels of detail for real-time animation. Graphics Interface. (1997).
This paper is the first SLOD paper I guess. They manually designed simplified dynamic models for particular system, in this case a legged creature. They used three levels of detail consisting of (1) rigid-body dynamic simulation, (2) point-mass model and kinematic model, and just (3) point-mass model only.

In (1), the system has three bodies (a hip and two parts of a telescoping leg) and four controlled degrees of freedom, such as pitch, roll and yaw of the body and the length of the leg. In (2) Hybrid kinematic/dynamic model, it "relies on a simple dynamic model for the motion of the body and computes the motion fo the leg kinematically". Lastly, (3) is equivalent to (2) without the kinematic model, i.e. the system computes only the position of the body on the playing field using simple point-mass model.

They used two different criteria for selecting appropriate level of detail: The first one is about the possibility of dynamic interactions among objects. For example, if a creature is very close to a wall, it should be simulated dynamically (Figure 5). The second one is about view-dependency such as whether it is in the field of view and if so, how close it is to the viewer (Figure 6).

#### Brogan, D.C. and Hodgins, J.K. 2002. Simulation level of detail for multiagent control. (New York, New York, USA, 2002), 199–206.
Summary goes here.

#### Chenney, S. and Forsyth, D. 1997. View-dependent culling of dynamic systems in virtual environments. (New York, New York, USA, 1997), 55–58.
View-dependent culling is different than SLOD. They stop simulating a dynamic system once it goes out of view, and then use statistical sampling to predict the current state of the system when it comes back to the view. Thus, what they are doing is literally "culling dynamics". They also utilize a human perception model to make the prediction more plausible and its errors less noticeable to human observer when the system goes in and out of the view (Consistency).

#### O'Brien, D. et al. 2001. Automatic simplification of particle system dynamics. (2001), 210–257.
This paper introduced an approach that automatically generates approximated motion model in order to be used in SLOD but the method is limited to particle systems only. Manual generation of simplifed models is one of major shortcomings of SLOD.

#### 1. Setas, M.N. and Gomes, M.R. 1995. Dynamic simulation of natural environments in virtual reality. … in Virtual Environments. (1995).
#### 2. Perbet, F. and Cani, M.-P. 2001. Animating prairies in real-time. (New York, New York, USA, 2001), 103–110.
These two papers are very similar.

#### Beaudoin, J. and Keyser, J. 2004. Simulation levels of detail for plant motion. (New York, New York, USA, 2004), 297–304.
Summary goes here.

#### Brom, C. et al. 2007. Simulation Level of Detail for Virtual Humans. Intelligent Virtual Agents. Springer Berlin Heidelberg. 1–14.
Summary goes here.

#### Ward, K. et al. 2003. Modeling hair using level-of-detail representations. (2003), 41–47.
Summary goes here.


### Category of View-dependent fluid simulation
Here are papers which add view-dependent criteria to conventional adaptive fluid simulation

#### Solenthaler, B. and Gross, M. 2011. Two-scale particle simulation. SIGGRAPH '11: SIGGRAPH 2011 papers. (Aug. 2011).
They used simple camera information, such as the field of view, to assign high-resolution region to the part of fluid currently in the view frustum.

#### Barran, B.A. 2006. View dependent fluid dynamics. (2006).

Interestingly, the author used a cylindrical coordinate system for computational grid instead of a Cartesian coordinate system in order to make it adaptive to perspective projection. Due to the use of cylindrical coordinates, the system has various cell sizes, which becomes larger as it goes far away from the origin (Figure 2).

#### 1. Bunlutangtum, R. and Kanongchaiyos, P. 2011. Adaptive Grid Refinement Using View-Dependent Octree for Grid-Based Smoke Simulation. Motion in Games. Springer Berlin Heidelberg. 204–215.
#### 2. Bunlutangtum, R. and Kanongchaiyos, P. 2011. Enhanced view-dependent adaptive grid refinement for animating fluids. (Dec. 2011).
#### 3. Kim, J. et al. 2006. View-dependent adaptive animation of liquids. ETRI journal. (2006).

Those three papers are very similar to one another. They used an octree in a Cartesian coordinate system for their computational grids, and then took into account camera information to refine their grids properly.

#### Yue Gao et al. 2013. View-Dependent Multiscale Fluid Simulation. IEEE Transactions on Visualization and Computer Graphics. 19, 2 (Feb. 2013), 178–188.
Summary goes here.


### Category of Adpative fluid simulations (No view-dependency)
#### Losasso, F. et al. 2004. Simulating water and smoke with an octree data structure. SIGGRAPH '04: SIGGRAPH 2004 Papers. (Aug. 2004).
This paper is one of the first adaptive fluid simulation papers (octree-based) so we might cite it when we mention those view-dependent fluid simulation papers.


## 2. Rendering
### Category of Geometric level-of-detail (GLOD)
Methods in this category switch to simplified model when the distance from camera is greater than thresholds.

#### 1. Duchaineau, M. et al. 1997. ROAMing terrain: Real-time Optimally Adapting Meshes. (1997), 81–88.
#### 2. Friedrich, A. et al. 1999. Smooth View-Dependent Rendering in Animations. (1999).
#### 3. Hinsinger, D. et al. 2002. Interactive animation of ocean waves. (New York, New York, USA, 2002), 161–166.
#### 4. Hoppe, H. 1998. Smooth view-dependent level-of-detail control and its application to terrain rendering. (1998), 35–42.
All the geometric level-of-detail papers are about rendering and I could find nothing specifically related to our project.


### Category of View-dependent GLOD (VGLOD)
Methods in this category use not only distance but also view frustum, occlusion, surface normal, screen-space projection and so on when choosing appropriate GLOD. They basically use view-dependency a lot, so there are a lot of criteria which seems useful to our project as well.

#### Xia, J.C. and Varshney, A. 1996. Dynamic view-dependent simplification for polygonal models. (1996), 327–334.
Section 3. Image-Space-Guided Simplification

1. Local illumition:
Increase detail in a direction perpendicular to, and propotional to, the illumination gradient across the surface. It also uses surface normal.
1. Screen-space projection:
Use projected length instead of object-space length.
1. Visibility culling:
Remove back-facing polygons.
1. Silhouette boundaries:
Use projected length of silhouette edges to contorol smoothness of slihouette.

#### Hoppe, H. 1997. View-dependent refinement of progressive meshes. (Aug. 1997).
Section 4. Refinement Criteria

1. View frustum
1. Surface orientation
1. Screen-space geometric error

#### Funkhouser, T.A. and Séquin, C.H. 1993. Adaptive display algorithm for interactive frame rates during visualization of complex virtual environments. (New York, New York, USA, 1993), 247–254.
This paper is one of the most interesting papers in this list. To begin with, this paper is about view-dependent rendering to achieve faster rendering speed by selecting appropriate GLOD and rendering algorithms for each object, such as float, Gouraud and Phong shading.

In contrast to previous GLOD papers, The main point of this paper is that they didn't set any static threshold for selecting LOD and rendering algorithm. Rather they made the system adaptively changes a threshold for selecting LOD to achieve uniform and bounded frame rate (Adaptive Detail Elision). In this process they rely on an optimization technique to counteract sudden changes of the complexity of scene due to a camera movement.

They mentioned two approaches for dynamic threshold: (1) Feedback and (2) Optimization. The first one adjusts the threshold based on the rendering time of the previous to meet the target frame rate.  However, this method basically assumes that the complexity of scene is smoothly changing, which is not true if the camera moves quickly or jumps to a very different location.  Thus, they opted for the second one, Optimization, which basically predicts the rendering time and the importance of each object in all possible configurations (every combination of LOD and rendering algorithm), and then renders objects in descending order of Value, which is a ratio of importance to rendering time, as long as the target frame rate allows. This is a greedy approximation because their original Optimization algorithm is NP-complete.

Section 5. Benefit Heuristic

1. Semantics
1. Focus
1. Motion blur
1. Hysteresis


## Et cetera
* Brooks, R.J. and Tobias, A.M. 1996. Choosing the best model: Level of detail, complexity, and model performance. Mathematical and Computer Modelling. 24, 4 (Aug. 1996), 1–14.
* Debunne, G. et al. 2000. Adaptive simulation of soft bodies in real-time. (2000), 15–20.
* Grzeszczuk, R. et al. 1998. NeuroAnimator. (New York, New York, USA, 1998), 9–20.
* Ko, H. and Badler, N.I. 1992. Straight Line Walking Animation Based on Kinematic Generalization that Preserves the Original Characteristics. (1992).
* Li, L. and Volkov, V. 2005. Cloth animation with adaptively refined meshes. Australian Computer Society, Inc.
* Lindstrom, P. and Pascucci, V. 2002. Terrain simplification simplified: a general framework for view-dependent out-of-core visualization. IEEE Transactions on Visualization and Computer Graphics. 8, 3 (2002), 239–254.
* Lindstrom, P. and Pascucci, V. 2001. Visualization of large terrains made easy. (2001), 363–574.
* Lindstrom, P. et al. 1996. Real-time, continuous level of detail rendering of height fields. (New York, New York, USA, 1996), 109–118.
* Liu, S.Q. et al. 2006. Real-time, dynamic level-of-detail management for three-axis NC milling simulation. Computer-Aided Design. 38, 4 (Apr. 2006), 378–391.
* Luebke, D. and Erikson, C. 1997. View-dependent simplification of arbitrary polygonal environments. (New York, New York, USA, 1997), 199–208.
* Müller, M. et al. 2003. Particle-based fluid simulation for interactive applications. (Jul. 2003).
* Thomaszewski, B. et al. 2007. Advanced Topics in Virtual Garment Simulation Part 1. (Aug. 2007), 1–23.
* Xia, J.C. et al. 1997. Adaptive real-time level-of-detail based rendering for polygonal models. IEEE Transactions on Visualization and Computer Graphics. 3, 2 (1997), 171–183.
* Yan, J. 1985. Advances in Computer-Generated Imagery for Flight Simulation. IEEE Computer Graphics and Applications. 5, 8 (Aug. 1985), 37–51.


## Not related?
* Popovic, Z. and Witkin, A. 1999. Physically based motion transformation. (New York, New York, USA, 1999), 11–20.
