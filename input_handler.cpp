//#include "input_handler.h"
//#include "MK64F12.h"
//
///**
// * This file contains the codebase for reading inputs from the NES controller.
// * The source code was implemented based on the guideline provided in the link below,
// *
// * https://www.allaboutcircuits.com/projects/nes-controller-interface-with-an-arduino-uno/
// *
// *
// * which shows the details of NES controller integration into Arduino UNO.
// * We modified the code accordingly so that the same logic can be applied to K64F.
// *
// *
// *
// *
// */
//
//
//const int CLOCK_GPIO_INDEX = 3;
//const int LATCH_GPIO_INDEX = 2;
//const int DATA_GPIO_INDEX  = 2;
//
//void set_clock_high() {
//    PTC->PSOR |= (1 << CLOCK_GPIO_INDEX);
//}
//
//void set_clock_low() {
//    PTC->PCOR |= (1 << CLOCK_GPIO_INDEX);
//}
//
//void set_latch_high() {
//    PTC->PSOR |= (1 << LATCH_GPIO_INDEX);
//}
//
//void set_latch_low() {
//    PTC->PCOR |= (1 << LATCH_GPIO_INDEX);
//}
//
//void initialize_input_handler() {
//    
//    // enable clock line
//    SIM->SCGC5 |= (1 << 11);
//    PORTC->PCR[CLOCK_GPIO_INDEX] = PORT_PCR_MUX(001);
//    // set the bit to output
//    PTC->PDDR |= (1 << CLOCK_GPIO_INDEX);
//    
//    // enable latch line
//    PORTC->PCR[LATCH_GPIO_INDEX] = PORT_PCR_MUX(001);
//    // set the bit to output
//    PTC->PDDR |= (1 << LATCH_GPIO_INDEX);
//    
//    // enable data line
//    SIM->SCGC5 |= (1 << 9);
//    PORTA->PCR[DATA_GPIO_INDEX] = PORT_PCR_MUX(001);
//    // clear the bit to input
//    PTA->PDDR &= ~(1 << DATA_GPIO_INDEX);
//    
//    // initialize the clock and latch to be high signal
//    set_clock_high();
//    set_latch_high();
//}
//
//int read_bit(void){
//    return ((PTA->PDIR >> DATA_GPIO_INDEX) & 1);
//}
//
//uint8_t read_data_input_from_input_handler() {
//    uint8_t key_pressed = 0;
//    
//    // initially low the clock and latch
//    set_clock_low();
//    set_latch_low();
//    
//    // toggle the latch so that the register detects the initial data bit to read
//    set_latch_high();
//    for (int d = 0; d < 2 * (DEFAULT_SYSTEM_CLOCK / 1000000); d++);
//    set_latch_low();
//    
//    key_pressed += read_bit();
//    
//    // for the next 7 bits, we toggle the clock signal and follow the same logic as above.
//    // In order to fit the bit into the right location, we should shift our bit by one before
//    // reading the bit from the data line.
//    for (int b = 0; b < 8; b++) {
//        
//        set_clock_high();
//        
//        for (int d = 0; d < 2 * (DEFAULT_SYSTEM_CLOCK / 1000000); d++);
//        
//        key_pressed <<= 1;
//        
//        key_pressed += read_bit();
//        
//        for (int d = 0; d < 4 * (DEFAULT_SYSTEM_CLOCK / 1000000); d++);
//        
//        set_clock_low();
//    }
//    
//    key_pressed = ~key_pressed;
//    
//    return key_pressed;
//}