module counter(out, clk, rst);
input wire clk, rst;
output reg [3:0]out;

always@(posedge clk)
begin
if (rst==1)
	out <= 4'b0000;
else 
	out <= out + 1;
end
endmodule
