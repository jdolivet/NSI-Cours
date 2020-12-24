BSim = {};

$(function() {
    var split = new SplitPane('#split-container', ['#editor-pane', '#simulation-pane']);

    $('.global-controls').append('<span style="margin-right:10px;">'+$('title').text()+'</span>');

    // initial configuration
    split.setPaneWidth(0, split.window_width());
    split.setPaneWidth(1, 0);

    // Set up the split buttons.
    $('#maximise_editor').click(function() {
        split.setPaneWidth(0, split.window_width());
        split.setPaneWidth(1, 0);
    });
    $('#split_pane').click(function() {
        var width = split.window_width();
        split.setPaneWidth(0, width/2);
        split.setPaneWidth(1, width/2);
    });
    $('#maximise_simulation').click(function() {
        split.setPaneWidth(0, 0);
        split.setPaneWidth(1, split.window_width());
    });

    split.on('resize', function(widths) {
        if(widths[1] === 0) {
            $('#maximise_editor').addClass('active').siblings().removeClass('active');
        } else if(widths[0] === 0) {
            $('#maximise_simulation').addClass('active').siblings().removeClass('active');
        } else {
            $('#split_pane').addClass('active').siblings().removeClass('active');
        }
        if(widths[0] === 0) {
            editor.blur();
        }
    });

    // Make an editor
    var editor = new Editor('#editor', 'uasm', true);
    editor.openTab('beta.uasm', 
`////////////////////////////////////////////////////////////////////////
/// 6.004 BETA Macro package -                  revised 1/25/16 SAW  ///
///  This file defines our 32-bit Beta instruction set.              ///
////////////////////////////////////////////////////////////////////////

/* Global instruction definition conventions:
 *  * DESTINATION arg is LAST
 *
 * Instruction set summary.  Notation:
 * ra, rb, rc: registers
 *         CC: 16-bit signed constant
 *      label: statement/location tag (becomes PC-relative offset)
 *
 * ADD(RA, RB, RC)      // RC <- <RA> + <RB>
 * ADDC(RA, C, RC)      // RC <- <RA> + C
 * AND(RA, RB, RC)      // RC <- <RA> & <RB>
 * ANDC(RA, C, RC)      // RC <- <RA> & C
 * MUL(RA, RB, RC)      // RC <- <RA> * <RB>
 * MULC(RA, C, RC)      // RC <- <RA> * C
 * DIV(RA, RB, RC)      // RC <- <RA> / <RB>
 * DIVC(RA, C, RC)      // RC <- <RA> / C
 * OR( RA, RB, RC)      // RC <- <RA> | <RB>
 * ORC(RA,  C, RC)      // RC <- <RA> | C
 * SHL(RA, RB, RC)      // RC <- <RA> << <RB>
 * SHLC(RA, C, RC)      // RC <- <RA> << C
 * SHR(RA, RB, RC)      // RC <- <RA> >> <RB>
 * SHRC(RA, C, RC)      // RC <- <RA> >> C
 * SRA(RA, RB, RC)      // RC <- <RA> >> <RB>
 * SRAC(RA, C, RC)      // RC <- <RA> >> C
 * SUB(RA, RB, RC)      // RC <- <RA> - <RB>
 * SUBC(RA, C, RC)      // RC <- <RA> - C
 * XOR(RA, RB, RC)      // RC <- <RA> ^ <RB>
 * XORC(RA, C, RC)      // RC <- <RA> ^ C
 * XNOR(RA, RB, RC)     // RC <- ~(<RA> ^ <RB>)
 * XNORC(RA, C, RC)     // RC <- ~(<RA> ^ C)
 *
 * CMPEQ(RA, RB, RC)    // RC <- <RA> == <RB>
 * CMPEQC(RA, C, RC)    // RC <- <RA> == C
 * CMPLE(RA, RB, RC)    // RC <- <RA> <= <RB>
 * CMPLEC(RA, C, RC)    // RC <- <RA> <= C
 * CMPLT(RA, RB, RC)    // RC <- <RA> <  <RB>
 * CMPLTC(RA, C, RC)    // RC <- <RA> <  C
 *
 *
 * BR(LABEL,RC)         // RC <- <PC>+4; PC <- LABEL (PC-relative addressing)
 * BR(LABEL)            // PC <- LABEL (PC-relative addressing)
 * BEQ(RA, LABEL, RC)   // RC <- <PC>+4; IF <RA>==0 THEN PC <- LABEL
 * BEQ(RA, LABEL)       // IF <RA>==0 THEN PC <- LABEL
 * BF(RA, LABEL, RC)    // RC <- <PC>+4; IF <RA>==0 THEN PC <- LABEL
 * BF(RA, LABEL)        // IF <RA>==0 THEN PC <- LABEL
 * BNE(RA, LABEL, RC)   // RC <- <PC>+4; IF <RA>!=0 THEN PC <- LABEL
 * BNE(RA, LABEL)       // IF <RA>!=0 THEN PC <- LABEL
 * BT(RA, LABEL, RC)    // RC <- <PC>+4; IF <RA>!=0 THEN PC <- LABEL
 * BT(RA, LABEL)        // IF <RA>!=0 THEN PC <- LABEL
 * JMP(RA, RC)          // RC <- <PC>+4; PC <- <RA> & 0xFFFC
 * JMP(RB)              // PC <- <RB> & 0xFFFC
 *
 * LD(RA, CC, RC)       // RC <- <<RA>+CC>
 * LD(CC, RC)           // RC <- <CC>
 * ST(RC, CC, RA)       // <RA>+CC <- <RC>
 * ST(RC, CC)           // CC <- <RC>
 * LDR(CC, RC)          // RC <- <CC> (PC-relative addressing)
 *
 * MOVE(RA, RC)         // RC <- <RA>
 * CMOVE(CC, RC)        // RC <- CC
 * HALT()               // STOPS SIMULATOR.
 *
 * PUSH(RA)             // (2) SP <- <SP> + 4; <<SP>-4> <- <RA>
 * POP(RA)              // (2) RA <- <<SP>-4>; SP <- <SP> - 4
 * ALLOCATE(N)          // Allocate N longwords from stack
 * DEALLOCATE(N)        // Release N longwords
 *
 * CALL(label)          // Call a subr; save PC in lp.
 * CALL(label, n)       // (2) Call subr at label with n args.
 *                      // Saves return adr in LP.
 *                      // Pops n longword args from stack.
 *
 * RTN()                // Returns to adr in <LP> (Subr return)
 * XRTN()               // Returns to adr in <IP> (Intr return)
 *
 * SHORT(val)           // Assemble val as a 16-bit datum
 * LONG(val)            // Assemble val as a 32-bit datum 
 * WORD(val)            // Assemble val as a 32-bit datum 
 *                      // (LONG and WORD are synonyms)
 * GETFRAME(F, RA)      // RA <- <<BP>+F>
 * PUTFRAME(RA, F)      // <BP>+F <- <RA>
 *
 * Calling convention:
 *      PUSH(argn-1)
 *      ...
 *      PUSH(arg0)
 *      CALL(subr, nargs)
 *      (return here with result in R0, args cleaned)
 *
 * Extra register conventions, for procedure linkage:
 * LP = 28              // Linkage register (holds return adr)
 * BP = 29              // Frame pointer (points to base of frame)
 *
 * Conventional stack frames look like:
 *      arg[N-1]
 *      ...
 *      arg[0]
 *      <saved lp>
 *      <saved bp>
 *      <other saved regs>
 *   BP-><locals>
 *       ...
 *   SP->(first unused location)
 */

////////////////////////////////////////////////////////////////////////
/// End of documentation.  Following are the actual definitions...   ///
////////////////////////////////////////////////////////////////////////

// Assemble words, little-endian:
.macro SHORT(x) x%0x100 (x>>8)%0x100 
.macro LONG(x) SHORT(x) SHORT(x >> 16)  // little-endian for Beta 
.macro WORD(x) SHORT(x) SHORT(x >> 16)  // Synonym for LONG

.macro STORAGE(NWORDS)  . = .+(4*NWORDS)// Reserve NWORDS words of RAM

// register designators
// this allows symbols like r0, etc to be used as
// operands in instructions. Note that there is no real difference
// in this assembler between register operands and small integers.

r0 = 0
r1 = 1
r2 = 2
r3 = 3
r4 = 4
r5 = 5
r6 = 6
r7 = 7
r8 = 8
r9 = 9
r10 = 10
r11 = 11
r12 = 12
r13 = 13
r14 = 14
r15 = 15
r16 = 16
r17 = 17
r18 = 18
r19 = 19
r20 = 20
r21 = 21
r22 = 22
r23 = 23
r24 = 24
r25 = 25
r26 = 26
r27 = 27
r28 = 28
r29 = 29
r30 = 30
r31 = 31

bp = 27                 // frame pointer (points to base of frame)
lp = 28                 // linkage register (holds return adr)
sp = 29                 // stack pointer (points to 1st free locn)
xp = 30                 // interrupt return pointer (lp for interrupts)


// understand upper case, too.
R0 = r0
R1 = r1
R2 = r2
R3 = r3
R4 = r4
R5 = r5
R6 = r6
R7 = r7
R8 = r8
R9 = r9
R10 = r10
R11 = r11
R12 = r12
R13 = r13
R14 = r14
R15 = r15
R16 = r16
R17 = r17
R18 = r18
R19 = r19
R20 = r20
R21 = r21
R22 = r22
R23 = r23
R24 = r24
R25 = r25
R26 = r26
R27 = r27
R28 = r28
R29 = r29
R30 = r30
R31 = r31
XP = xp
LP = lp
BP = bp
SP = sp

.macro betaop(OP,RA,RB,RC) {
          .align 4
          WORD((OP<<26)+((RC%0x20)<<21)+((RA%0x20)<<16)+((RB%0x20)<<11)) }

.macro betaopc(OP,RA,CC,RC) {
          .align 4
          WORD((OP<<26)+((RC%0x20)<<21)+((RA%0x20)<<16)+(CC%0x10000)) }


.macro ADD(RA, RB, RC)          betaop(0x20,RA,RB,RC)
.macro ADDC(RA, C, RC)          betaopc(0x30,RA,C,RC)

.macro AND(RA, RB, RC)          betaop(0x28,RA,RB,RC)
.macro ANDC(RA, C, RC)          betaopc(0x38,RA,C,RC)
.macro MUL(RA, RB, RC)          betaop(0x22,RA,RB,RC)
.macro MULC(RA, C, RC)          betaopc(0x32,RA,C,RC)
.macro DIV(RA, RB, RC)          betaop(0x23,RA,RB,RC)
.macro DIVC(RA, C, RC)          betaopc(0x33,RA,C,RC)
.macro OR( RA, RB, RC)          betaop(0x29,RA,RB,RC)
.macro ORC(RA,  C, RC)          betaopc(0x39,RA,C,RC)
.macro SHL(RA, RB, RC)          betaop(0x2C,RA,RB,RC)
.macro SHLC(RA, C, RC)          betaopc(0x3C,RA,C,RC)
.macro SHR(RA, RB, RC)          betaop(0x2D,RA,RB,RC)
.macro SHRC(RA, C, RC)          betaopc(0x3D,RA,C,RC)
.macro SRA(RA, RB, RC)          betaop(0x2E,RA,RB,RC)
.macro SRAC(RA, C, RC)          betaopc(0x3E,RA,C,RC)
.macro SUB(RA, RB, RC)          betaop(0x21,RA,RB,RC)
.macro SUBC(RA, C, RC)          betaopc(0x31,RA,C,RC)
.macro XOR(RA, RB, RC)          betaop(0x2A,RA,RB,RC)
.macro XORC(RA, C, RC)          betaopc(0x3A,RA,C,RC)
.macro XNOR(RA, RB, RC)         betaop(0x2B,RA,RB,RC)
.macro XNORC(RA, C, RC)         betaopc(0x3B,RA,C,RC)

.macro CMPEQ(RA, RB, RC)        betaop(0x24,RA,RB,RC)
.macro CMPEQC(RA, C, RC)        betaopc(0x34,RA,C,RC)
.macro CMPLE(RA, RB, RC)        betaop(0x26,RA,RB,RC)
.macro CMPLEC(RA, C, RC)        betaopc(0x36,RA,C,RC)
.macro CMPLT(RA, RB, RC)        betaop(0x25,RA,RB,RC)
.macro CMPLTC(RA, C, RC)        betaopc(0x35,RA,C,RC)

.macro BETABR(OP,RA,RC,LABEL)   betaopc(OP,RA,((LABEL-.)>>2)-1, RC)
.macro BEQ(RA, LABEL, RC)       BETABR(0x1C,RA,RC,LABEL)
.macro BEQ(RA, LABEL)           BETABR(0x1C,RA,r31,LABEL)
.macro BF(RA, LABEL, RC)        BEQ(RA,LABEL,RC)
.macro BF(RA,LABEL)             BEQ(RA,LABEL)
.macro BNE(RA, LABEL, RC)       BETABR(0x1D,RA,RC,LABEL)
.macro BNE(RA, LABEL)           BETABR(0x1D,RA,r31,LABEL)
.macro BT(RA,LABEL,RC)          BNE(RA,LABEL,RC)
.macro BT(RA,LABEL)             BNE(RA,LABEL)
.macro BR(LABEL,RC)             BEQ(r31, LABEL, RC)
.macro BR(LABEL)                BR(LABEL, r31)
.macro JMP(RA, RC)              betaopc(0x1B,RA,0,RC)
.macro JMP(RA)                  betaopc(0x1B,RA,0,r31)

.macro LD(RA, CC, RC)           betaopc(0x18,RA,CC,RC)
.macro LD(CC, RC)               betaopc(0x18,R31,CC,RC)
.macro ST(RC, CC, RA)           betaopc(0x19,RA,CC,RC)
.macro ST(RC, CC)               betaopc(0x19,R31,CC,RC)
.macro LDR(CC, RC)              BETABR(0x1F, R31, RC, CC)

.macro MOVE(RA, RC)             ADD(RA, R31, RC)
.macro CMOVE(CC, RC)            ADDC(R31, CC, RC)

.macro PUSH(RA)         ADDC(SP,4,SP)  ST(RA,-4,SP)
.macro POP(RA)          LD(SP,-4,RA)   ADDC(SP,-4,SP)

.macro CALL(label)      BR(label, LP)
                        
.macro RTN()            JMP(LP)
.macro XRTN()           JMP(XP)

// Controversial Extras
// Calling convention:
//      PUSH(argn-1)
//      ...
//      PUSH(arg0)
//      CALL(subr, nargs)
//      (return here with result in R0, args cleaned)

// Extra register conventions, for procedure linkage:
// LP = 28                      // Linkage register (holds return adr)
// BP = 29                      // Frame pointer (points to base of frame)

// Conventional stack frames look like:
//      arg[N-1]
//      ...
//      arg[0]
//      <saved lp>
//      <saved bp>
//      <other saved regs>
//   BP-><locals>
//       ...
//   SP->(first unused location)

.macro CALL(S,N) BR(S,lp) SUBC(sp, 4*N, sp)

.macro ALLOCATE(N) ADDC(sp, N*4, sp)
.macro DEALLOCATE(N) SUBC(sp, N*4, sp)

//--------------------------------------------------------
// Privileged mode instructions
//--------------------------------------------------------

.macro PRIV_OP(FNCODE)          betaopc (0x00, 0, FNCODE, 0)
.macro HALT() PRIV_OP (0)
.macro RDCHAR() PRIV_OP (1)
.macro WRCHAR() PRIV_OP (2)
.macro CYCLE()  PRIV_OP (3)
.macro TIME()   PRIV_OP (4)
.macro CLICK()  PRIV_OP (5)
.macro RANDOM() PRIV_OP (6)
.macro SEED()   PRIV_OP (7)
.macro SERVER() PRIV_OP (8)

// SVC calls; used for OS extensions

.macro SVC(code)                betaopc (0x01, 0, code, 0)

// Trap and interrupt vectors
VEC_RESET       = 0             // Reset (powerup)
VEC_II          = 4             // Illegal instruction (also SVC call)
VEC_CLK         = 8             // Clock interrupt
VEC_KBD         = 12            // Keyboard interrupt
VEC_MOUSE       = 16            // Mouse interrupt

// constant for the supervisor bit in the PC
PC_SUPERVISOR      = 0x80000000         // the bit itself
PC_MASK            = 0x7fffffff         // a mask for the rest of the PC

// The following macros save and restore all 32 registers (including R31) in
// a 32-word block of memory.  There are two versions:
//   * single-argument version, whose argument WHERE must be a location
//     in low memory (i.e., addressable via a 16-bit signed offset); and
//   * 2-argument version, which includes a constant offset and a base
//     register (as in LD and ST).
// NB: That location must be in low memory, i.e., addressable by a
// 16-bit signed offset.

.macro save_all_regs(WHERE) save_all_regs(WHERE, r31)
.macro save_all_regs(WHERE, base_reg) {
        ST(r0,WHERE,base_reg)
        ST(r1,WHERE+4,base_reg)
        ST(r2,WHERE+8,base_reg)
        ST(r3,WHERE+12,base_reg)
        ST(r4,WHERE+16,base_reg)
        ST(r5,WHERE+20,base_reg)
        ST(r6,WHERE+24,base_reg)
        ST(r7,WHERE+28,base_reg)
        ST(r8,WHERE+32,base_reg)
        ST(r9,WHERE+36,base_reg)
        ST(r10,WHERE+40,base_reg)
        ST(r11,WHERE+44,base_reg)
        ST(r12,WHERE+48,base_reg)
        ST(r13,WHERE+52,base_reg)
        ST(r14,WHERE+56,base_reg)
        ST(r15,WHERE+60,base_reg)
        ST(r16,WHERE+64,base_reg)
        ST(r17,WHERE+68,base_reg)
        ST(r18,WHERE+72,base_reg)
        ST(r19,WHERE+76,base_reg)
        ST(r20,WHERE+80,base_reg)
        ST(r21,WHERE+84,base_reg)
        ST(r22,WHERE+88,base_reg)
        ST(r23,WHERE+92,base_reg)
        ST(r24,WHERE+96,base_reg)
        ST(r25,WHERE+100,base_reg)
        ST(r26,WHERE+104,base_reg)
        ST(r27,WHERE+108,base_reg)
        ST(r28,WHERE+112,base_reg)
        ST(r29,WHERE+116,base_reg)
        ST(r30,WHERE+120,base_reg)
        ST(base_reg,WHERE+124,base_reg)
} // End of save-all-regs macro

.macro restore_all_regs(WHERE) restore_all_regs(WHERE, r31)
.macro restore_all_regs(WHERE, base_reg) {
        LD(base_reg,WHERE,r0)
        LD(base_reg,WHERE+4,r1)
        LD(base_reg,WHERE+8,r2)
        LD(base_reg,WHERE+12,r3)
        LD(base_reg,WHERE+16,r4)
        LD(base_reg,WHERE+20,r5)
        LD(base_reg,WHERE+24,r6)
        LD(base_reg,WHERE+28,r7)
        LD(base_reg,WHERE+32,r8)
        LD(base_reg,WHERE+36,r9)
        LD(base_reg,WHERE+40,r10)
        LD(base_reg,WHERE+44,r11)
        LD(base_reg,WHERE+48,r12)
        LD(base_reg,WHERE+52,r13)
        LD(base_reg,WHERE+56,r14)
        LD(base_reg,WHERE+60,r15)
        LD(base_reg,WHERE+64,r16)
        LD(base_reg,WHERE+68,r17)
        LD(base_reg,WHERE+72,r18)
        LD(base_reg,WHERE+76,r19)
        LD(base_reg,WHERE+80,r20)
        LD(base_reg,WHERE+84,r21)
        LD(base_reg,WHERE+88,r22)
        LD(base_reg,WHERE+92,r23)
        LD(base_reg,WHERE+96,r24)
        LD(base_reg,WHERE+100,r25)
        LD(base_reg,WHERE+104,r26)
        LD(base_reg,WHERE+108,r27)
        LD(base_reg,WHERE+112,r28)
        LD(base_reg,WHERE+116,r29)
        LD(base_reg,WHERE+120,r30)
} // End of restore-all-regs macro

/// Macro to extract and right-adjust a bit field from RA, and leave it
/// in RB.  The bit field M:N, where M >= N.
.macro extract_field (RA, M, N, RB) {
       SHLC(RA, 31-M, RB)       // Shift left, to mask out high bits
       SHRC(RB, 31-(M-N), RB)   // Shift right, to mask out low bits.
}

// Macro to reserve N consecutive WORDS of memory:
.macro RESERVE(N) . = .+(N*4)

`     
     ,true);
    
    
    editor.openTab('TinyOS +', 
`////////////////////////////////////////////////////////////////////////
/// TinyOS: Simple OS demo for 6.004 Beta processor
////////////////////////////////////////////////////////////////////////

//  This program implements a primitive OS kernel for the Beta
//  along with four simple user-mode processes hooked together thru
//  a semaphore-controlled bounded buffer.
//
//  The four processes -- and the kernel -- share an address space;
//  each is allocated its own stack (for a total of 4 stacks), and
//  each process has its own virtual machine state (ie, registers).
//  The latter is stored in the kernel ProcTbl, which contains a data
//  structure for each process.

// Here's an unretouched sample of output from a BSIM run of the demo:
// 
// Start typing, Bunky.
//                                                
// 00000000> hello
// ELLOHAY
// 

.include "beta.uasm"		// Define Beta instructions, etc.
.options clock tty

// The following code is a primitive but complete timesharing kernel
//  sufficient to run four processes, plus handlers for a small
//  selection of supervisor calls (SVCs) to perform OS services.
//  The latter include simple console I/O and semaphores.
//
// All kernel code is executed with the Kernel-mode bit of the
//  program counter -- its high-order bit --- set.  This causes
//  new interrupt requests to be deferred until the kernel returns
//  to user mode.

// Interrupt vectors:

. = VEC_RESET
	BR(I_Reset)	// on Reset (start-up)
. = VEC_II
	BR(I_IllOp)	// on Illegal Instruction (eg SVC)
. = VEC_CLK
	BR(I_Clk)	// on clock interrupt
. = VEC_KBD
	BR(I_Kbd)	// on Keyboard interrupt
. = VEC_MOUSE
	BR(I_Mouse)	// on mouse interrupt

// The following macro is the first instruction to be entered for each
// asynchronous I/O interrupt handler.	 It adjusts XP (the interrupted
// PC) to account for the instruction skipped due to the pipeline bubble.
.macro ENTER_INTERRUPT() SUBC(XP,4,XP)

////////////////////////////////////////////////////////////////////////
/// Kernel Interrupt support code
/// We use a slightly simpler (and less efficient) scheme here from
///  that in the text.  On kernel entry, the ENTIRE state -- 31
///  registers -- of the interrupted program is saved in a designated
///  region of kernel memory ("UserMState", below).  This entire state
///  is then restored on return to the interrupted program.
////////////////////////////////////////////////////////////////////////

// Here's the SAVED STATE of the interrupted process, while we're
// processing an interrupt.
UserMState:
        STORAGE(32)     // R0-R31... (PC is in XP!)

// Here are macros to SAVE and RESTORE state -- 31 registers -- from
//   the above storage.

// N.B. - The following macro assumes that R0 is a macro for
// the integer 0, R1 is a macro for the integer 1, etc.
.macro SS(R) ST(R, UserMState+(4*R))    // (Auxiliary macro)

.macro SAVESTATE() {
		SS(0)  SS(1)  SS(2)  SS(3)  SS(4)  SS(5)  SS(6)	 SS(7)
		SS(8)  SS(9)  SS(10) SS(11) SS(12) SS(13) SS(14) SS(15)
		SS(16) SS(17) SS(18) SS(19) SS(20) SS(21) SS(22) SS(23)
		SS(24) SS(25) SS(26) SS(27) SS(28) SS(29) SS(30) }

// See comment for SS(R), above
.macro RS(R) LD(UserMState+(4*R), R)    // (Auxiliary macro)

.macro RESTORESTATE() {
        RS(0)  RS(1)  RS(2)  RS(3)  RS(4)  RS(5)  RS(6)  RS(7)
        RS(8)  RS(9)  RS(10) RS(11) RS(12) RS(13) RS(14) RS(15)
        RS(16) RS(17) RS(18) RS(19) RS(20) RS(21) RS(22) RS(23)
        RS(24) RS(25) RS(26) RS(27) RS(28) RS(29) RS(30) }

KStack: LONG(.+4)               // Pointer to ...
        STORAGE(256)            //  ... the kernel stack.

//////////////////////////////////////////////////////////////////////////////
/// Handler for unexpected interrupts
//////////////////////////////////////////////////////////////////////////////

I_BadInt:
        CALL(KWrMsg)                    // Type out an error msg,
        .text "Unexpected interrupt..."
        HALT()
        

//////////////////////////////////////////////////////////////////////////////
/// Handler for Illegal Instructions
///  (including SVCs)
//////////////////////////////////////////////////////////////////////////////

I_IllOp:
        SAVESTATE()             // Save the machine state.
        LD(KStack, SP)          // Install kernel stack pointer.

        LD(XP, -4, r0)          // Fetch the illegal instruction
        SHRC(r0, 26, r0)        // Extract the 6-bit OPCODE
        SHLC(r0, 2, r0)         // Make it a WORD (4-byte) index
        LD(r0, UUOTbl, r0)      // Fetch UUOTbl[OPCODE]
        JMP(r0)                 // and dispatch to the UUO handler.

.macro UUO(ADR) LONG(ADR+PC_SUPERVISOR)	// Auxiliary Macros
.macro BAD()	UUO(UUOError)


UUOTbl: BAD()           UUO(SVC_UUO)    BAD()           BAD()
        BAD()           BAD()           BAD()           BAD()
        BAD()           BAD()           BAD()           BAD()
        BAD()           BAD()           BAD()           BAD()
        BAD()           BAD()           BAD()           BAD()
        BAD()           BAD()           BAD()           BAD()
        BAD()           BAD()           BAD()           BAD()
        BAD()           BAD()           BAD()           BAD()
        BAD()           BAD()           BAD()           BAD()
        BAD()           BAD()           BAD()           BAD()
        BAD()           BAD()           BAD()           BAD()
        BAD()           BAD()           BAD()           BAD()
        BAD()           BAD()           BAD()           BAD()
        BAD()           BAD()           BAD()           BAD()
        BAD()           BAD()           BAD()           BAD()
        BAD()           BAD()           BAD()           BAD()

// Here's the handler for truly unused opcodes (not SVCs):
UUOError:
        CALL(KWrMsg)                    // Type out an error msg,
        .text "Illegal instruction "
        LD(xp, -4, r0)                  //   giving hex instr and location;
        CALL(KHexPrt)
        CALL(KWrMsg)
        .text " at location 0x"
        MOVE(xp,r0)
        CALL(KHexPrt)
        CALL(KWrMsg)
        .text "! ....."
        HALT()                          // Then crash system.

// Here's the common exit sequence from Kernel interrupt handlers:
// Restore registers, and jump back to the interrupted user-mode
// program.

I_Rtn:  RESTORESTATE()
kexit:  JMP(XP)                 // Good place for debugging breakpoint!

// Alternate return from interrupt handler which BACKS UP PC,
// and calls the scheduler prior to returning.   This causes
// the trapped SVC to be re-executed when the process is
// eventually rescheduled...

I_Wait: LD(UserMState+(4*30), r0)       // Grab XP from saved MState,
        SUBC(r0, 4, r0)                 // back it up to point to
        ST(r0, UserMState+(4*30))       //    SVC instruction

        CALL(Scheduler)                 // Switch current process,
        BR(I_Rtn)                       // and return to (some) user.

// Sub-handler for SVCs, called from I_IllOp on SVC opcode::

SVC_UUO:
		LD(XP, -4, r0)			// The faulting instruction.
 		ANDC(r0,15,r0)			// Pick out low bits,
		SHLC(r0,2,r0)			// make a word index,
		LD(r0,SVCTbl,r0)		// and fetch the table entry.
		JMP(r0)

SVCTbl:	UUO(HaltH)				// SVC(0): User-mode HALT instruction
		UUO(WrMsgH)				// SVC(1): Write message
		UUO(WrChH)				// SVC(2): Write Character
		UUO(GetKeyH)			// SVC(3): Get Key
		UUO(HexPrtH)			// SVC(4): Hex Print
		UUO(WaitH)				// SVC(5): Wait(S) ,,, S in R3
		UUO(SignalH)			// SVC(6): Signal(S), S in R3
		UUO(YieldH)				// SVC(7): Yield()
		UUO(MouseH)				// SVC(8): Get mouse click


////////////////////////////////////////////////////////////////////////
// Keyboard handling
////////////////////////////////////////////////////////////////////////

Key_State: LONG(0)                      // 1-char keyboard buffer.

GetKeyH:                                // return key code in r0, or block
        LD(Key_State, r0)
        BEQ(r0, I_Wait)                 // on 0, just wait a while

// key ready, return it and clear the key buffer
        LD(Key_State, r0)               // Fetch character to return
        ST(r0,UserMState)               // return it in R0.
        ST(r31, Key_State)              // Clear kbd buffer
        BR(I_Rtn)                       // and return to user.


// Interrupt side: read key, store it into buffer.
// NB: This is a LIGHTWEIGHT interrupt handler, which doesn't
//   do a full state save.  It doesn't have to, since (1) it
//   only uses R0, and (2) it always returns to the same process
//   it interrupts.  By not saving all state, it manages
//   to save a LOT of time:  20 STs on entry, 30 LDs on exit:
I_Kbd:  ENTER_INTERRUPT()               // Adjust the PC!
        ST(r0, UserMState)              // Save ONLY r0...
        RDCHAR()                        // Read the character,
        ST(r0,Key_State)                // save its code.
        LD(UserMState, r0)              // restore r0, and
        JMP(xp)                         // and return to the user.

WrChH:  LD(UserMState,r0)               // The user's R0
        WRCHAR()                        // Write out the character,
        BR(I_Rtn)                       // then return

WrMsgH: LD(UserMState+(4*30), r0)       // Fetch interrupted XP, then
        CALL(KMsgAux)                   // print text following SVC.
        ST(r0,UserMState+(4*30))        // Store updated XP.
        BR(I_Rtn)

// Handler for HexPrt(): print hex value from R0
HexPrtH:
        LD(UserMState,r0)               // Load user R0
        CALL(KHexPrt)                   // Print it out 
        BR(I_Rtn)                       // And return to user.


////////////////////////////////////////////////////////////////////////
/// Mouse handling
////////////////////////////////////////////////////////////////////////

Mouse_State: LONG(-1)

MouseH:                					// return mouse code in r0, or block
    	LD(Mouse_State, r0)
    	CMPEQC(r0, -1, r1)
    	BNE(r1, I_Wait)       			// if r0 == -1, wait a while

// mouse info ready, return it and clear the mouse buffer
    	LD(Mouse_State, r0)   			// Fetch mouse state to return
    	ST(r0, UserMState)    			// return it in r0
    	CMOVE(-1, r1)
    	ST(r1, Mouse_State)  			// clear the mouse state storage
    	BR(I_Rtn)             			// then return

I_Mouse:
    	ENTER_INTERRUPT()				// Adjust the PC!
    	ST(r0, UserMState)    			// Save r0
    	CLICK()               			// Read in information from click
    	ST(r0, Mouse_State)   			// Store it into the Mouse_State
    	LD(UserMState, r0)    			// Restore r0
//.breakpoint
    	JMP(xp)               			// return to the user
       

//////////////////////////////////////////////////////////////////////////////
/// Timesharing: 4-process round-robin scheduler
//////////////////////////////////////////////////////////////////////////////

// ProcTbl contains a 31-word data structure for each process,
//  including R0-R30.  R31, which always contains 0, is omitted.
//  The XP (R30) value stored for each process is the PC,
//  and points to the next instruction to be executed.

// The kernel variable CurProc always points to the ProcTbl entry
//  corresponding to the "swapped in" process.

ProcTbl:
        STORAGE(29)             	// Process 0: R0-R28
        LONG(P0Stack)           	// Process 0: SP
        LONG(P0Start)           	// Process 0: XP (= PC)

        STORAGE(29)             	// Process 1: R0-R28
        LONG(P1Stack)           	// Process 1: SP
        LONG(P1Start)           	// Process 1: XP (= PC)

        STORAGE(29)             	// Process 2: R0-R28
        LONG(P2Stack)           	// Process 2: SP
        LONG(P2Start)           	// Process 2: XP (= PC)

		STORAGE(29)					// Process 3: R0-R28
    	LONG(P3Stack)  				// Process 3: SP 
    	LONG(P3Start)  				// Process 3: XP (= PC)
           

CurProc: LONG(ProcTbl)

// Schedule a new process.
// Swaps current process out of UserMState, swaps in a new one.

Scheduler:
        PUSH(LP)
        CMOVE(UserMState, r0)
        LD(CurProc, r1)
        CALL(CopyMState)                // Copy UserMState -> CurProc

        LD(CurProc, r0)
        ADDC(r0, 4*31, r0)              // Increment to next process..
        CMPLTC(r0,CurProc, r1)          // End of ProcTbl?
        BT(r1, Sched1)                  // Nope, its OK.
        CMOVE(ProcTbl, r0)              // yup, back to Process 0.
Sched1: ST(r0, CurProc)                 // Here's the new process;

        ADDC(r31, UserMState, r1)       // Swap new process in.
        CALL(CopyMState)
        LD(Tics, r0)                    // Reset TicsLeft counter
        ST(r0, TicsLeft)                //   to Tics.
        POP(LP)
        JMP(LP)                         // and return to caller.

// Copy a 31-word MState structure from the address in r0 to that in r1
// Trashes r2, leaves r0-r1 unchanged.
.macro CM(N) LD(r0, N*4, r2)  ST(r2, N*4, r1)   // Auxiliary macro
CopyMState:
        CM(0)   CM(1)   CM(2)   CM(3)   CM(4)   CM(5)   CM(6)   CM(7)
        CM(8)   CM(9)   CM(10)  CM(11)  CM(12)  CM(13)  CM(14)  CM(15)
        CM(16)  CM(17)  CM(18)  CM(19)  CM(20)  CM(21)  CM(22)  CM(23)
        CM(24)  CM(25)  CM(26)  CM(27)  CM(28)  CM(29)  CM(30)
        JMP(LP)

//////////////////////////////////////////////////////////////////////////////
/// Clock interrupt handler:  Invoke the scheduler.
//////////////////////////////////////////////////////////////////////////////

/// Here's the deal:
/// Each compute-bound process gets a quantum consisting of TICS clock
///   interrupts, where TICS is the number stored in the variable Tics
///   below.  To avoid overhead, we do a full state save only when the
///   clock interrupt will cause a process swap, using the TicsLeft
///   variable as a counter.
/// We do a LIMITED state save (r0 only) in order to free up a register,
///   then count down TicsLeft stored below.  When it becomes negative,
///   we do a FULL state save and call the scheduler; otherwise we just
///   return, having burned only a few clock cycles on the interrupt.
/// RECALL that the call to Scheduler sets TicsLeft to Tics, giving
///   the newly-swapped-in process a full quantum.

Tics:   LONG(2)                 // Number of clock interrupts/quantum.
TicsLeft: LONG(0)               // Number of tics left in this quantum

I_Clk:  ENTER_INTERRUPT()       // Adjust the PC!
        ST(r0, UserMState)      // Save R0 ONLY, for now.
        LD(TicsLeft, r0)        // Count down TicsLeft
        SUBC(r0,1,r0)
        ST(r0, TicsLeft)        // Now there's one left.
        CMPLTC(r0, 0, r0)       // If new value is negative, then
        BT(r0, DoSwap)          //   swap processes.
        LD(UserMState, r0)      // Else restore r0, and
        JMP(XP)                 // return to same user.

DoSwap: LD(UserMState, r0)      // Restore r0, so we can do a
        SAVESTATE()             //   FULL State save.
        LD(KStack, SP)          // Install kernel stack pointer.
        CALL(Scheduler)         // Swap it out!
        BR(I_Rtn)               // and return to next process.


////////////////////////////////////////////////////////////////////////
/// yield() SVC: voluntarily give up rest of time quantum.
////////////////////////////////////////////////////////////////////////

YieldH: CALL(Scheduler)         // Schedule next process, and
        BR(I_Rtn)               // and return to user.


//////////////////////////////////////////////////////////////////////////////
/// Here on start-up (reset):  Begin executing process 0.
//////////////////////////////////////////////////////////////////////////////

I_Reset:
        CMOVE(P0Stack, SP)
        CMOVE(P0Start, XP)
        JMP(XP)


//////////////////////////////////////////////////////////////////////////////
/// SVC Sub-handler for user-mode HALTs
//////////////////////////////////////////////////////////////////////////////

HaltH:  BR(I_Wait)          	// SVC(0): User-mode HALT SVC


//////////////////////////////////////////////////////////////////////////////
/// Kernel support for User-mode Semaphores
//////////////////////////////////////////////////////////////////////////////


/// User-mode access: macrodefinitions.  Semaphore adr passed in r3,
///  which is saved and restored appropriately by macros:
/// NB: Wait() and Signal() SVCs each pass the address of a semaphore
///  in R3.  Since the Illegal Opcode handler code doesn't change any
///  registers except R0, the R3 semaphore address is still intact
///  when we enter these handlers:

/// Kernel handler: wait(s):
/// ADDRESS of semaphore s in r3.

WaitH:  LD(r3,0,r0)             // Fetch semaphore value.
        BEQ(r0,I_Wait)          // If zero, block..

        SUBC(r0,1,r0)           // else, decrement and return.
        ST(r0,0,r3)             // Store back into semaphore
        BR(I_Rtn)               // and return to user.

/// Kernel handler: signal(s):
/// ADDRESS of semaphore s in r3.

SignalH:LD(r3,0,r0)             // Fetch semaphore value.
        ADDC(r0,1,r0)           // increment it,
        ST(r0,0,r3)             // Store new semaphore value.
        BR(I_Rtn)               // and return to user.

//////////////////////////////////////////////////////////////////////////////
/// Kernel-callable Utility Routines
/// NB: These routines use PRIVILEDGED instructions; hence they can be
///  called directly only from kernel code (ie, with the high-PC-bit
///  set).  Use SVC traps to accomplish the same functions from user-
///  level code.
//////////////////////////////////////////////////////////////////////////////


/// Hex print procedure: prints longword in R0

HexDig: LONG('0') LONG('1') LONG('2') LONG('3') LONG('4') LONG('5')
        LONG('6') LONG('7') LONG('8') LONG('9') LONG('A') LONG('B')
        LONG('C') LONG('D') LONG('E') LONG('F')

KHexPrt:
        PUSH(r0)                // Saves all regs, incl r0
        PUSH(r1)
        PUSH(r2)
        PUSH(lp)

        CMOVE(8, r2)
        MOVE(r0,r1)
KHexPr1:
        SRAC(r1,28,r0)                  // Extract digit into r0.
        MULC(r1, 16, r1)                // Next loop, next nybble...
        ANDC(r0, 0xF, r0)
        MULC(r0, 4, r0)
        LD(r0, HexDig, r0)
        WRCHAR ()
        SUBC(r2,1,r2)
        BNE(r2,KHexPr1)

        POP(lp)
        POP(r2)
        POP(r1)
        POP(r0)
        RTN()

////////////////////////////////////////////////////////////////////////
/// Procedure to print out a zero-terminated message, packed one     ///
///    char/byte. Char data follows branch; returns to next 4-byte   ///
///    aligned location. Saves all regs.                             ///
////////////////////////////////////////////////////////////////////////

KWrMsg:
        PUSH (R0)
        MOVE(LP, R0)
        CALL(KMsgAux)
        MOVE(R0, LP)
        POP (R0)
        RTN()


// Auxiliary routine for sending a message to the console.
// On entry, R0 should point to data; on return, R0 holds next
// longword aligned location after data.
// Note: Must be called while in supervisor mode.

KMsgAux:
        PUSH(r1)
        PUSH(r2)
        PUSH(r3)
        PUSH(r4)

        MOVE (R0, R1)

WrWord: LD (R1, 0, R2)          // Fetch a 4-byte word into R2
        ADDC (R1, 4, R1)        // Increment word pointer
        CMOVE(4,r3)             // Byte/word counter

WrByte: ANDC(r2, 0x7F, r0)      // Grab next byte -- LOW end first!
        BEQ(r0, WrEnd)          // Zero byte means end of text.
        WRCHAR()                // Print it.
        SRAC(r2,8,r2)           // Shift out this byte
        SUBC(r3,1,r3)           // Count down... done with this word?
        BNE(r3,WrByte)          // Nope, continue.
        BR(WrWord)              // Yup, on to next.

WrEnd:
        MOVE (R1, R0)
        POP(r4)
        POP(r3)
        POP(r2)
        POP(r1)
        RTN()

//////////////////////////////////////////////////////////////////////////////
/// User-mode code.  Includes 4 processes:
///
/// PROCESS 0:
///   (1) Prompts the user for new lines of input.
///   (2) Reads lines from the keyboard (using the GetKey() SVC),
///       and pipes it to PROCESS 1 through a bounded buffer.
///       It does this using the Send procedure.
///
/// PROCESS 1:
///   Reads lines of input from PROCESS 0, using the Rcv procedure,
///       translates them to Piglatin, and types them out (using
///       the SVCs WrCh() and WrMsg().
///
///   Note that Send and Rcv, used by processes 0 and 1, communicate
///       using a bounded buffer and synchronize using semaphores
///       implemented as the Wait(S) and Signal(S) SVCs.
///
/// PROCESS 2:
///   On each quantum, simply increments a counter and uses the Yield()
///       SVC to give up the remainder of its quantum.  The resulting
///       count thus becomes a count of the number of quanta which have
///       been allocated to each process.  This count (in HEX) is used
///       as the prompt typed by process 0.
/// 
/// PROCESS 3:
///   On each click with the mouse calls Mouse() and then prints out 
/// 		the X and Y coordinates of the click.
/// 	  That click message only appear after the prompt has been output 
/// 		but before typing in a sentence to be translated.
/// 	  The coordinate printout should happen immediately unless 
/// 	    it's delayed because the user has started typing.
///   Note : If the user clicks multiple times after started typing, 
///         it will produce two click messages: 
/// 	      one for the first click and one for the last click.
///
//////////////////////////////////////////////////////////////////////////////

/// Definitions of macros used to interface with Kernel code:

.macro Halt()   SVC(0)          // Stop a process.

.macro WrMsg()  SVC(1)          // Write the 0-terminated msg following SVC
.macro WrCh()   SVC(2)          // Write a character whose code is in R0

.macro GetKey() SVC(3)          // Read a key from the keyboard into R0
.macro HexPrt() SVC(4)          // Hex Print the value in R0.

.macro Yield()  SVC(7)          // Give up remaining quantum
.macro Mouse()  SVC(8)          // Read the coordinate information form most recent couse click

/// Semaphore macros.
/// Wait(S) waits on semaphore S; Signal(S) signals on S.
/// Both preserve all registers, by pushing and popping R3.

.macro Wait(S) {
        PUSH(r3)                // Save old r3,
        LDR(S,r3)               // put semaphore address into r3
        SVC(5)                  // Wait on semaphore whose adr is in R3
        POP(r3) }               // and restore former r3

.macro Signal(S) {
        PUSH(r3)                // Save old r3,
        LDR(S,r3)               // put semaphore address into r3
        SVC(6)                  // Signal on semaphore whose adr is in R3
        POP(r3) }               // and restore former r3

/// Allocate a semaphore: used like
///    name:   semaphore(size)
.macro semaphore(N) {           // Allocate a semaphore, and build a ptr
   LONG(.+4)                    // Pointer to semaphore
   LONG(N) }                    // Semaphore itself, init value N.

//////////////////////////////////////////////////////////////////////////////
/// User-mode code: Process 0
//////////////////////////////////////////////////////////////////////////////

Prompt: semaphore(1)            // To keep us from typing next prompt
								// while P1 is typing previous output.

P0Start:WrMsg()
		.text "Start typing, Bunky.\\n\\n"

P0Read:	Wait(Prompt)			// Wait until P1 has caught up...
		WrMsg()					// First a newline character, then
		.text "\\n"
		LD(Count3, r0)			// print out the quantum count
		HexPrt()				//  as part of the count, then
		WrMsg()					//  the remainder.
		.text "> "
		
	Signal(Mse_Click)			// Signal on Mouse click
	
		LD(P0LinP, r3)			// ...then read a line into buffer...
		
		GetKey()				// read next character,
	Wait(Mse_Click)				// Wait on semaphore
		WrCh()					// echo back to user
		CALL(UCase)				// Convert it to upper case,
		ST(r0,0,r3)				// Store it in buffer.
		ADDC(r3,4,r3)			// Incr pointer to next char...

		CMPEQC(r0,0xA,r1)		// End of line?
		BT(r1,P0Send)			// yup, transmit buffer to P1

P0RdCh: GetKey()                // read next character,

        WrCh()                  // echo back to user
        CALL(UCase)             // Convert it to upper case,
        ST(r0,0,r3)             // Store it in buffer.
        ADDC(r3,4,r3)           // Incr pointer to next char...

        CMPEQC(r0,0xA,r1)       // End of line?
        BT(r1,P0Send)           // yup, transmit buffer to P1

        CMPEQC(r3,P0LinP-4,r1)  // are we at end of buffer?
        BF(r1,P0RdCh)           // nope, read another char
        CMOVE(0xA,r0)           // end of buffer, force a newline
        ST(r0,0,r3)
        WrCh()                  // and echo it to the user

P0Send: LD(P0LinP,r2)           // Prepare to empty buffer.
P0PutC: LD(r2,0,r0)             // read next char from buf,
        CALL(Send)              // send to P1
        CMPEQC(r0,0xA,r1)       // Is it end of line?
        BT(r1,P0Read)           // Yup, read another line.

        ADDC(r2,4,r2)           // Else move to next char.
        BR(P0PutC)

P0Line: STORAGE(100)            // Line buffer.
P0LinP: LONG(P0Line)

P0Stack: STORAGE(256)			// Stack for process 0.


////////////////////////////////////////////////////////////////////////
/// Some auxilliaries for our little application:
////////////////////////////////////////////////////////////////////////

// Auxilliary routine: convert char in r0 to upper case:
UCase:  PUSH(r1)
        CMPLEC(r0,'z',r1)       // Is it beyond 'z'?
        BF(r1,UCase1)           // yup, don't convert.
        CMPLTC(r0,'a',r1)       // Is it before 'a'?
        BT(r1, UCase1)          // yup, no change.
        SUBC(r0,'a'-'A',r0)     // Map to UPPER CASE...
UCase1: POP(r1)
        RTN()

// Auxilliary routine: Test if r0 is a vowel; boolean into r1.
VowelP: CMPEQC(r0,'A',r1)       // Sorta brute force...
        BT(r1,Vowel1)
        CMPEQC(r0,'E',r1)       BT(r1,Vowel1)
        CMPEQC(r0,'I',r1)       BT(r1,Vowel1)
        CMPEQC(r0,'O',r1)       BT(r1,Vowel1)
        CMPEQC(r0,'U',r1)       BT(r1,Vowel1)
        CMPEQC(r0,'Y',r1)       BT(r1,Vowel1)
        CMOVE(0,r1)             // Return FALSE.
Vowel1: RTN()

////////////////////////////////////////////////////////////////////////
/// Bounded-buffer FIFO routines for Beta USER MODE
///  CALL(Send) - sends datum in r0 thru pipe
///  CALL(Rcv)  - reads datum from pipe into r0
////////////////////////////////////////////////////////////////////////

FIFOSIZE = 100
FIFO:   STORAGE(FIFOSIZE)       // FIFO buffer.

IN:     LONG(0)                 // IN pointer: index into FIFO
OUT:    LONG(0)                 // OUT pointer: index into FIFO

Chars:  semaphore(0)            // Flow-control semaphore 1
Holes:  semaphore(FIFOSIZE)     // Flow-control semaphore 2

// Send: put r0 into fifo.
Send:   PUSH(r1)                // Save some regs...
        PUSH(r2)
        Wait(Holes)             // Wait for space in buffer...

        LD(IN,r1)               // IN pointer...
        MULC(r1,4,r2)           // Compute 4*IN, word offset
        ST(r0,FIFO,r2)          // FIFO[IN] = ch
        ADDC(r1,1,r1)           // Next time, next slot.
        CMPEQC(r1,FIFOSIZE,r2)  // End of buffer?
        BF(r2,Send1)            // nope.
        CMOVE(0,r1)             // yup, wrap around.
Send1:  ST(r1,IN)               // Tuck away input pointer

        Signal(Chars)           // Now another Rcv() can happen
        POP(R2)
        POP(r1)
        RTN()

// Rcv: Get char from fifo into r0.

Rcv:    PUSH(r1)
        PUSH(r2)
        Wait(Chars)             // Wait until FIFO non-empty

        LD(OUT,r1)              // OUT pointer...
        MULC(r1,4,r2)           // Compute 4*OUT, word offset
        LD(r2,FIFO,r0)          // result = FIFO[OUT]
        ADDC(r1,1,r1)           // Next time, next slot.
        CMPEQC(r1,FIFOSIZE,r2)  // End of buffer?
        BF(r2,Rcv1)             // nope.
        CMOVE(0,r1)             // yup, wrap around.
Rcv1:   ST(r1,OUT)              // Tuck away input pointer

        Signal(Holes)           // Now theres space for 1 more.
        POP(R2)
        POP(r1)
        RTN()

////////////////////////////////////////////////////////////////////////
/// USER MODE Process 1: Translate English to Piglatin
////////////////////////////////////////////////////////////////////////

P1Start:
        LD(P1BufP, r9)          // Buffer pointer in r9.

P1Word: MOVE(r9,r5)             // Read initial consonants.
P1Cons: CALL(Rcv)
        CALL(VowelP)            // Is it a vowel?
        BT(r1,P1Vowl)           // yup, move on.
        CMPLEC(r0,' ',r1)       // Is it white space?
        BT(r1,P1Spc)

        ST(r0,0,r5)             // Else store it into buffer...
        ADDC(r5,4,r5)           // ... and bump pointer.
        BR(P1Cons)              // Back for more.

P1Vowl: WrCh()                  // Output the vowel,
        CALL(Rcv)               // then check again.
        CMPLEC(r0,' ',r1)       // White space?
        BF(r1,P1Vowl)

P1Spc:  MOVE(r0,r3)             // Save input char, then
        MOVE(r9,r4)             // Output initial consonant.
P1Spc2: CMPEQ(r4,r5,r1)         // Any left?
        BT(r1,P1Spc1)           // nope...
        LD(r4,0,r0)             // Fetch next char,
        ADDC(r4,4,r4)           // (next time, next char)
        WrCh()                  // and write it out.
        BR(P1Spc2)

P1Spc1: WrMsg()                 // Add the "AY" suffix.
        .text "AY"
        MOVE(r3,r0)             // Then the saved input char.
        WrCh()
        CMPEQC(r3,0xA,r0)       // Was it end-of-line?
        BF(r0,P1Word)           // nope.

		Signal(Prompt)			// it was; allow proc 0 to re-prompt.
        BR(P1Word)              // ... and start another word.

P1Buf:  STORAGE(100)            // Line buffer.
P1BufP: LONG(P1Buf)             // Address of line buffer.
P1Stack: STORAGE(256)           // Stack for process 1.

////////////////////////////////////////////////////////////////////////
/// USER MODE Process 2: Simply counts quanta.
////////////////////////////////////////////////////////////////////////

P2Start:
        LD(Count3, r0)          // Another quantum, incr count3.
        ADDC(r0,1,r0)
        ST(r0,Count3)
        Yield()                 // Invoke scheduler
        BR(P2Start)             // return here after others run.

P2Stack: STORAGE(256)			// Stack for process 2.

Count3: LONG(0)

////////////////////////////////////////////////////////////////////////
/// USER MODE Process 3: Process that Reports Mouse Clicks
////////////////////////////////////////////////////////////////////////

Mse_Click: semaphore(0)			// To keep us from output mouse click
								// while P0 is going on

P3Start:
		Mouse()					// Read the coordinate information	
	Wait(Mse_Click)				// Wait until the semaphore is ready 
		LD(UserMState, r0)    	// load click value into r0
		
		ADD(r0, r31, r1)		// Get the x value
		SHRC(r0, 16, r0)      
		ST(r0, UserMState)

		WrMsg()					// Print the x value
		.text "\\nClick at x="
		HexPrt()

		SHLC(r1, 16 ,r1)		// Get the y value
		SHRC(r1, 16, r1)
		ADD(r1, r31, r0)
		ST(r0, UserMState)

		WrMsg()					// Print the y value
		.text ", y="
		HexPrt()
		
		WrMsg()					// Print the new line
		.text "\\n"
		LD(Count3, r0)			// print out the quantum count
		HexPrt()				//  as part of the count, then
		WrMsg()					//  the remainder.
		.text "> "
		
	Signal(Mse_Click)			// Let up the semaphore 
		BR(P3Start)             // and go back to the start

P3Stack: STORAGE(256)			// Stack for process 3.
`
, true);
    $('.editor-file-control').hide();     // hide file buttons
    $('#editor .nav-tabs .close').hide();  // hide close button on tab(s)

    var do_assemble = function() {
        var filename = editor.currentTab();
        var content = editor.content('assemble');
        var metadata = editor.metadata();
        var assembler = new BetaAssembler(editor);
        editor.clearErrors();
        assembler.assemble(filename, content, metadata, function(success, result) {
            if(!success) {
                PassiveAlert("Assembly failed.", "error");
                _.each(result, function(error) {
                    if(!_.contains(editor.filenames(), error.file)) {
                        editor.openFile(error.file, true, function(editor_filename, content) {
                            editor.markErrorLine(editor_filename, error.message, error.line - 1, error.column);
                        });
                    } else {
                        editor.markErrorLine(error.file, error.message, error.line - 1, error.column);
                    }
                });
            } else {
                PassiveAlert("Assembled successfully", "success");
                beta.setSources(result.sources);
                beta.loadBytes(result.image,result.source_map);
                beta.setBreakpoints(result.breakpoints);
                beta.setLabels(result.labels);
                _.each(result.options, function(value, key) {
                    beta.setOption(key, value);
                });
                beta.getMemory().setProtectedRegions(result.protection);
                if(result.checkoff) {
                    if(result.checkoff.kind == 'tty') {
                        beta.setVerifier(new BSim.TextVerifier(beta, result.checkoff));
                    } else if(result.checkoff.kind == 'memory') {
                        beta.setVerifier(new BSim.MemoryVerifier(beta, result.checkoff));
                    }
                } else {
                    beta.setVerifier(null);
                }
                if(split.currentState()[1] === 0) {
                    $('#maximise_simulation').click();
                }
            }
        });
    };

    // Add some buttons to it
    editor.addButtonGroup([new ToolbarButton('Assemble', do_assemble, 'Runs your program!')]);

    function window_height() {
        return $('.xblock-6004').innerHeight();
    };

    var set_height = function() {
        editor.setHeight(window_height() - $('.btn-toolbar').height() - $('.nav-tabs').height()); // Set height to window height minus title.
    };
    set_height();
    $(window).resize(set_height); // Update the height whenever the browser window changes size.
    split.on('resize', _.throttle(editor.redraw, 50));

    // Stuff for the simulator
    var do_resize = function(holder, view, difference) {
        if(holder.parents('#programmer-view').length) {
            $(window).resize(function() {
                var height = window_height() - difference;
                view.resize(height);
                holder.css({height: height});
            });
        }
    };

    var beta = new BSim.Beta(80); // This starting number is basically irrelevant

    $('.regfile').each(function() {
        new BSim.RegfileView(this, beta);
    });

    $('.tty').each(function() {
        new BSim.TTY(this, beta);
    });

    $('.disassembly').each(function() {
        var view = new BSim.DisassembledView(this, beta);
        do_resize($(this), view, 470);
    });

    $('.memory').each(function() {
        var view = new BSim.MemoryView(this, beta);
        do_resize($(this), view, 272);
    });

    $('.stack').each(function() {
        var view = new BSim.StackView(this, beta);
        do_resize($(this), view, 272);
    });

    new BSim.Beta.ErrorHandler(beta);
    var schematic = new BSim.SchematicView($('svg.schematic'), beta);
    split.on('resize', BSim.SchematicView.Scale);
    $(window).resize(BSim.SchematicView.Scale);

    $('.program-controls').each(function() {
        controls = new BSim.Controls(this, beta, editor, schematic);
    });

    // Work around weird sizing bug.
    _.delay(function() {
        $(window).resize();
    }, 10);

    // // Convenient way of loading a file for testing and such.
    // var neuter = function(e) {
    //     e.stopPropagation();
    //     e.preventDefault();
    // };
    // $('body').on('dragenter', neuter);
    // $('body').on('dragover', neuter);
    // $('body').on('drop', function(e) {
    //     neuter(e);
    //     console.log(e);
    //     var dt = e.originalEvent.dataTransfer;
    //     var files = dt.files;

    //     if(files.length === 0) return;
    //     var file = files[0];
    //     beta.stop(); // Just in case.
    //     var reader = new FileReader();
    //     reader.onload = function(e) {
    //         console.log(e);
    //         //beta = new BSim.Beta(e.target.result.length);
    //         var result = new Uint8Array(e.target.result);
    //         beta.loadBytes(result);
    //         console.log("Loaded", result.length, "bytes");
    //     };
    //     reader.readAsArrayBuffer(file);
    // });

    // For debugging
    window.beta = beta;
    window.editor = editor;

    //////////////////////////////////////////////////    
    //  edX interface
    //////////////////////////////////////////////////    

    var configuration = {};  // all state saved by edX server
    var controls;

    function update_tests() {
        try {
            var checkoff = controls.get_checkoff();
            if (checkoff !== undefined) {
                // key is checksum
                configuration.tests = checkoff;
            }
        } catch(e) {
            // do nothing...
        }
    }

    // return JSON representation to be used by server-side grader
    BSim.getGrade = function () {
        update_tests();
        var grade = {'tests': configuration.tests || {}};
        if (configuration.required_tests)
          grade.required_tests = configuration.required_tests;
        return JSON.stringify(grade);
    };

    // return JSON representation of persistent state
    BSim.getState = function () {
        update_tests();

        // start with all the ancillary information
        var state = $.extend({},configuration);
        delete state.initial_state;

        // gather up contents of editor buffers
        state.state = editor.get_all_documents(true);

        return JSON.stringify(state);
    };

    // process incoming state from jsinput framework
    // This function will be called with 1 argument when JSChannel is not used,
    // 2 otherwise. In the latter case, the first argument is a transaction 
    // object that will not be used here (see http://mozilla.github.io/jschannel/docs/)
    BSim.setState = function () {
        var stateStr = arguments.length === 1 ? arguments[0] : arguments[1];
        setTimeout(function () { BSim.setStateSync(stateStr); },1);
    };

    // 6.004 uses synchronous version...
    BSim.setStateSync = function (stateStr) {
        configuration = JSON.parse(stateStr);

        // open editor tabs for each saved buffer
        editor.closeAllTabs();
        var first = true;
        $.each(configuration.initial_state || {},
               function (name,contents) {
                   editor.openTab(name,contents,false,null,true);
               });
        $.each(configuration.state || {},
               function (name,contents) {
                   editor.openTab(name,contents,first);
                   first = false;
               });

        $('.editor-file-control').hide();     // hide file buttons
        $('#editor .nav-tabs .close').hide();  // hide close button on tab(s)
    };
    
    // if we're in an iframe...
    if (window.parent !== window) {
        // make iframe resizable if we can.  This may fail if we don't have
        // access to our parent...
        try {
            // look through all our parent's iframes
            $('iframe',window.parent.document).each(function () {
                // is this iframe us?
                if (this.contentWindow == window) {
                    // yes! so add css to enable resizing
                    $(this).css({resize:'both', overflow:'auto'});

                    // initial state is JSON stored as text child of <iframe>
                    var state = JSON.parse($(this).text() || '{}');

                    // grab our server-side state from the appropriate input field
                    var id = $(this).attr('data-id');
                    if (id) {
                        var input = $("[name='"+id+"']",window.parent.document);
                        if (input) {
                            // overwrite with user's state from server
                            input = input.val();
                            if (input.length > 0) {
                                var args = JSON.parse(input);
                                args.student_id = window.parent.anonymous_student_id;
                                $.extend(state,args);
                            }
                        }
                    }

                    BSim.setStateSync(JSON.stringify(state));
                }
            });
        } catch (e) {
        }
    }

});
