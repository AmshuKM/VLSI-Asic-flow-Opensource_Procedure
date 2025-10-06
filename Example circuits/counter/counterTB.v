module counterTB;
reg clk,rst;
wire [3:0]out;

    counter dut (
        .clk(clk),
        .rst(rst),
        .out(out)
    );
  
    initial begin
    $dumpfile("counterTB.vcd");
    $dumpvars(0,counterTB);
    end
    	initial begin
    
        clk = 0;
        forever #5 clk = ~clk;
        end
        
        initial begin
        rst = 0; // Assert reset (active-low)
        #30;rst = 1'b1; // Release reset
	#30 rst =0;
	
        #200; // Let the simulation run for 200ns
	$finish;      
    end

endmodule
