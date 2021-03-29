#!/usr/bin/env python
#! -*- coding:utf-8 -*-

''' Add the cladding model of MCNP about the HCF '''

import math

def CentralLocation(r, origin_theta, theta):
    x = r * math.cos((origin_theta + theta) * math.pi / 180)
    y = r * math.sin((origin_theta + theta) * math.pi / 180)
    return x, y


# judge the plates to be positive or negative
def PlatePositive(target_x, target_y, A, B, negative_D):
    if A*target_x + B*target_y + negative_D > 0:
        return 1
    else:
        return -1


# write the material card 
def MaterialCard(filename):
    with open(filename, "w") as f:
        f.write("m1 1001 1.0\n");
        f.write("m2 8016 1.0\n");


# main function
# diag_radius and the axis_radius are the inner circle
# clad_diag_radius and the clad_axis_radius are the outter circle
def Main(plate_cnt, 
         R, r, 
         low, high, 
         diag_radius, axis_raidus, 
         clad_diag_radius, clad_axis_radius, 
         surface_cnt, cell_cnt, original_surface_cnt,
         material_type):
    
    # judge the material type first
    if material_type == 1:  # HCF
        material_number = 1
        material_density = -2.7764
        universe = 1
    elif material_type == 2: # posion rod
        material_number = 4
        material_density = -9.8
        universe = 4
    elif material_type == 3: # graphite rod
        material_number = 3
        material_density = -2.266
        universe = 3
    
    with open("surface.txt", "a") as f_surface, open("cell.txt", "a") as f_cell:
        d_theta = 360 / plate_cnt
        d_h = (high-low) / plate_cnt
        for i in range(plate_cnt):
            X1, Y1 = CentralLocation(R, 45, i*d_theta)
            X2, Y2 = CentralLocation(R, 135, i*d_theta)
            X3, Y3 = CentralLocation(R, 225, i*d_theta)
            X4, Y4 = CentralLocation(R, 315, i*d_theta)
            x1, y1 = CentralLocation(r, 0, i*d_theta)
            x2, y2 = CentralLocation(r, 90, i*d_theta)
            x3, y3 = CentralLocation(r, 180, i*d_theta)
            x4, y4 = CentralLocation(r, 270, i*d_theta)
            print("===================================")
            print("X1=%f, Y1=%f" % (X1, Y1))
            print("X2=%f, Y2=%f" % (X2, Y2))
            print("X3=%f, Y3=%f" % (X3, Y3))
            print("X4=%f, Y4=%f" % (X4, Y4))

            print("x1=%f, y1=%f" % (x1, y1))
            print("x2=%f, y2=%f" % (x2, y2))
            print("x3=%f, y3=%f" % (x3, y3))
            print("x4=%f, y4=%f" % (x4, y4))
            print("===================================")
            
            # get the plate function
            theta = i*d_theta
            if 0 < theta < 90:
                k1 = math.tan((90 + (theta % 90)) * math.pi/180)
                A1 = -k1
                D1 = -x1 * k1 + y1
                
                k2 = -1 / k1
                A2 = -k2
                D2 = -x2 * k2 + y2
                
                k3 = k1
                A3 = -k3
                D3 = -x3 * k3 + y3
                
                k4 = k2
                A4 = -k4
                D4 = -x4 * k4 + y4
                B1 = B2 = B3 = B4 = 1.0
            elif 90 < theta < 180:
                k4 = math.tan((90 + (theta % 90)) * math.pi/180)
                A4 = -k4
                D4 = -x4 * k4 + y4
                
                k2 = k4
                A2 = -k2
                D2 = -x2 * k2 + y2
                
                k3 = -1 / k4
                A3 =  -k3
                D3 = -x3 * k3 + y3
                
                k1 = k3
                A1 = -k1
                D1 = -x1 * k1 + y1
                B1 = B2 = B3 = B4 = 1.0
            elif 180 < theta < 270:
                k3 = math.tan((90 + (theta % 90)) * math.pi/180)
                A3 = -k3
                D3 = -x3 * k3 + y3
                
                k1 = k3
                A1 = -k1
                D1 = -x1 * k1 + y1
                
                k2 = -1 / k3
                A2 = -k2
                D2 = -x2 * k2 + y2
                
                k4 = k2
                A4 = -k4
                D4 = -x4 * k4 + y4
                B1 = B2 = B3 = B4 = 1.0
            elif 270 < theta < 360:
                k2 = math.tan((90 + (theta % 90)) * math.pi/180)
                A2 = -k2
                D2 = -x2 * k2 + y2
                
                k4 = k2
                A4 = -k4
                D4 = -x4 * k4 + y4
                
                k3 = -1 / k2
                A3 = -k3
                D3 = -x3 * k3 + y3
                
                k1 = k3
                A1 = -k1
                D1 = -x1 * k1 + y1
                B1 = B2 = B3 = B4 = 1.0
            elif theta % 90 == 0:
                A1 = 1.0
                B1 = 0.0
                D1 = R / math.sqrt(2)
                
                A2 = 0.0
                B2 = 1.0
                D2 = R / math.sqrt(2)
                
                A3 = 1.0
                B3 = 0.0
                D3 = -R / math.sqrt(2)
                
                A4 = 0.0
                B4 = 1.0
                D4 = -R / math.sqrt(2)
            
            # if we choose the HCF type, then we write down the surface card, 
            # the posion rod and the control rod we do not need to write the surface card, only write the cell card is enough.
            if material_type == 1:
                ###############################################################
                #                       SURFACE CARD                          #
                ###############################################################
                # plate surface
                f_surface.write("%d P %f %f %f %f\n" % (surface_cnt, A1, B1, 0.0, D1))                # original_surface_cnt + 0
                surface_cnt += 1                                                                      
                f_surface.write("%d P %f %f %f %f\n" % (surface_cnt, A2, B2, 0.0, D2))                # original_surface_cnt + 1
                surface_cnt += 1                                                                      
                f_surface.write("%d P %f %f %f %f\n" % (surface_cnt, A3, B3, 0.0, D3))                # original_surface_cnt + 2
                surface_cnt += 1                                                                      
                f_surface.write("%d P %f %f %f %f\n" % (surface_cnt, A4, B4, 0.0, D4))                # original_surface_cnt + 3
                surface_cnt += 1                                                                      
                f_surface.write("%d PZ %f\n" % (surface_cnt, low + i*d_h))                            # original_surface_cnt + 4
                surface_cnt += 1                                                                      
                f_surface.write("%d PZ %f\n" %(surface_cnt, low + (i+1)*d_h))                         # original_surface_cnt + 5
                surface_cnt += 1
    
                # large cylinder which is INSIDE.
                f_surface.write("%d C/Z %f %f %f\n" % (surface_cnt, X1, Y1, diag_radius))             # original_surface_cnt + 6
                surface_cnt += 1
                f_surface.write("%d C/Z %f %f %f\n" % (surface_cnt, X2, Y2, diag_radius))             # original_surface_cnt + 7
                surface_cnt += 1
                f_surface.write("%d C/Z %f %f %f\n" % (surface_cnt, X3, Y3, diag_radius))             # original_surface_cnt + 8
                surface_cnt += 1
                f_surface.write("%d C/Z %f %f %f\n" % (surface_cnt, X4, Y4, diag_radius))             # original_surface_cnt + 9
                surface_cnt += 1
    
                # litte cylinder which is INSIDE.
                f_surface.write("%d C/Z %f %f %f\n" % (surface_cnt, x1, y1, axis_raidus))             # original_surface_cnt + 10
                surface_cnt += 1
                f_surface.write("%d C/Z %f %f %f\n" % (surface_cnt, x2, y2, axis_raidus))             # original_surface_cnt + 11
                surface_cnt += 1
                f_surface.write("%d C/Z %f %f %f\n" % (surface_cnt, x3, y3, axis_raidus))             # original_surface_cnt + 12
                surface_cnt += 1
                f_surface.write("%d C/Z %f %f %f\n" % (surface_cnt, x4, y4, axis_raidus))             # original_surface_cnt + 13
                surface_cnt += 1
                
                # large cylinder which is OUTSIDE.
                f_surface.write("%d C/Z %f %f %f\n" % (surface_cnt, X1, Y1, clad_diag_radius))        # original_surface_cnt + 14
                surface_cnt += 1
                f_surface.write("%d C/Z %f %f %f\n" % (surface_cnt, X2, Y2, clad_diag_radius))        # original_surface_cnt + 15
                surface_cnt += 1
                f_surface.write("%d C/Z %f %f %f\n" % (surface_cnt, X3, Y3, clad_diag_radius))        # original_surface_cnt + 16
                surface_cnt += 1
                f_surface.write("%d C/Z %f %f %f\n" % (surface_cnt, X4, Y4, clad_diag_radius))        # original_surface_cnt + 17
                surface_cnt += 1
                
                # little cylinder which is OUTSIDE.
                f_surface.write("%d C/Z %f %f %f\n" % (surface_cnt, x1, y1, clad_axis_radius))        # original_surface_cnt + 18
                surface_cnt += 1
                f_surface.write("%d C/Z %f %f %f\n" % (surface_cnt, x2, y2, clad_axis_radius))        # original_surface_cnt + 19
                surface_cnt += 1
                f_surface.write("%d C/Z %f %f %f\n" % (surface_cnt, x3, y3, clad_axis_radius))        # original_surface_cnt + 20
                surface_cnt += 1
                f_surface.write("%d C/Z %f %f %f\n" % (surface_cnt, x4, y4, clad_axis_radius))        # original_surface_cnt + 21
                surface_cnt += 1
            
            ###############################################################
            #                       CELL CARD                             #
            ###############################################################
            ''' inner HCF model '''
            string = "%d %d %.3f %d %d %d %d %d -%d & \n" % (cell_cnt, 
                      material_number, material_density,
                      PlatePositive(0, 0, A1, 1.0, -D1)*(original_surface_cnt+0),
                      PlatePositive(0, 0, A2, 1.0, -D2)*(original_surface_cnt+1),
                      PlatePositive(0, 0, A3, 1.0, -D3)*(original_surface_cnt+2),
                      PlatePositive(0, 0, A4, 1.0, -D4)*(original_surface_cnt+3),
                      original_surface_cnt+4,
                      original_surface_cnt+5)
            string = string + "     (%d %d -%d) (%d %d -%d) & \n      (%d %d -%d) (%d %d -%d) & \n" % (
                      original_surface_cnt+6, original_surface_cnt+4, original_surface_cnt+5,
                      original_surface_cnt+7, original_surface_cnt+4, original_surface_cnt+5,
                      original_surface_cnt+8, original_surface_cnt+4, original_surface_cnt+5,
                      original_surface_cnt+9, original_surface_cnt+4, original_surface_cnt+5)
            string = string + "     :(-%d %d -%d):(-%d %d -%d): & \n      (-%d %d -%d):(-%d %d -%d) u=%d imp:n=1\n" % (
                      original_surface_cnt+10, original_surface_cnt+4, original_surface_cnt+5,
                      original_surface_cnt+11, original_surface_cnt+4, original_surface_cnt+5,
                      original_surface_cnt+12, original_surface_cnt+4, original_surface_cnt+5,
                      original_surface_cnt+13, original_surface_cnt+4, original_surface_cnt+5,
                      universe)
            
            cell_cnt += 1
            
            ''' the HCF cladding model '''
            string = string + "%d 3 -2.266 (%d %d %d %d %d -%d & \n" % (cell_cnt, 
                      PlatePositive(0, 0, A1, 1.0, -D1)*(original_surface_cnt+0),
                      PlatePositive(0, 0, A2, 1.0, -D2)*(original_surface_cnt+1),
                      PlatePositive(0, 0, A3, 1.0, -D3)*(original_surface_cnt+2),
                      PlatePositive(0, 0, A4, 1.0, -D4)*(original_surface_cnt+3),
                      original_surface_cnt+4,
                      original_surface_cnt+5) 
            string = string + "     (%d %d -%d) (%d %d -%d) & \n      (%d %d -%d) (%d %d -%d) & \n" % (
                      original_surface_cnt+14, original_surface_cnt+4, original_surface_cnt+5,
                      original_surface_cnt+15, original_surface_cnt+4, original_surface_cnt+5,
                      original_surface_cnt+16, original_surface_cnt+4, original_surface_cnt+5,
                      original_surface_cnt+17, original_surface_cnt+4, original_surface_cnt+5)
            string = string + "     :(-%d %d -%d):(-%d %d -%d): & \n      (-%d %d -%d):(-%d %d -%d)) #%d u=%d imp:n=1\n" % (
                      original_surface_cnt+18, original_surface_cnt+4, original_surface_cnt+5,
                      original_surface_cnt+19, original_surface_cnt+4, original_surface_cnt+5,
                      original_surface_cnt+20, original_surface_cnt+4, original_surface_cnt+5,
                      original_surface_cnt+21, original_surface_cnt+4, original_surface_cnt+5,
                      cell_cnt-1,
                      universe)
            
            cell_cnt += 1
            
            string = string + "%d 2 -1.94 -%d %d -%d #%d #%d u=%d imp:n=1\n" % (cell_cnt, 
                                                                     29000,
                                                                     original_surface_cnt+4, original_surface_cnt+5, 
                                                                     cell_cnt-1, cell_cnt-2,
                                                                     universe)
            
            cell_cnt += 1
            
            # the graphite rod the the posion rod also used to get the original_surface_cnt,
            # but we should trace back the first time original_surface_cnt (use record_original_surface_cnt)
            # and use the record_origianl_surface_cnt to be the parameter to be used in the next function.
            if i == 0:
                record_original_surface_cnt = original_surface_cnt
            else:
                pass
            
            # this command must be under from the record_origianl_surface_cnt.
            original_surface_cnt += 22
            
            f_cell.write(string)
    
    return surface_cnt, cell_cnt, original_surface_cnt, record_original_surface_cnt


if __name__ == '__main__':
    
    # TYPE 
    HCF = 1
    posion_rod = 2
    graphite_rod = 3
    
    plate_cnt = 12
    surface_cnt, cell_cnt, original_surface_cnt = 1, 1, 1
    
    for i in range(5):
        surface_cnt, cell_cnt, original_surface_cnt, record_original_surface_cnt = Main(plate_cnt, 
                                                           1.2075*math.sqrt(2), 1.2075, 
                                                           i*80,   (i+1)*80,  
                                                           0.8845, 0.3225, 
                                                           0.8045, 0.4025, 
                                                           surface_cnt, cell_cnt, original_surface_cnt,
                                                           HCF)
        surface_cnt, cell_cnt, original_surface_cnt, record_original_surface_cnt = Main(plate_cnt, 
                                                           1.2075*math.sqrt(2), 1.2075, 
                                                           i*80,   (i+1)*80,  
                                                           0.8845, 0.3225, 
                                                           0.8045, 0.4025, 
                                                           surface_cnt, cell_cnt, record_original_surface_cnt,
                                                           posion_rod)
        surface_cnt, cell_cnt, original_surface_cnt, record_original_surface_cnt = Main(plate_cnt, 
                                                           1.2075*math.sqrt(2), 1.2075, 
                                                           i*80,   (i+1)*80,  
                                                           0.8845, 0.3225, 
                                                           0.8045, 0.4025, 
                                                           surface_cnt, cell_cnt, record_original_surface_cnt,
                                                           graphite_rod)
    
    print("Done...\n")