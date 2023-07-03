from manim import *
from math import cos, sin


class Proof(Scene):
    def construct(self):
        
        title = Text("Euler's Formula:").to_edge(UP, buff=1)
        
        eq0 = MathTex(r"e^{i\theta} + 1 = 0")

        eq1= MathTex("{{e}}", "=" ,"{{(}}","{{1}}","{{+}}","\\frac{1}{n}",")^{n}")
        limit1 = MathTex(r"\lim_{n\to\infty}").next_to(eq1,RIGHT,buff=1)
        eq2= MathTex("{{e}}","^{x}", "=" ,"{{[}}","{{(}}","{{1}}","{{+}}","\\frac{1}{n}",")^{n}","{{]}}","^{x}")
        eq3= MathTex("{{e}}","^{x}", "=","{{(}}","{{1}}","{{+}}","\\frac{1}{n}",")^{nx}")
        eq4= MathTex("{{e}}","^{x}", "=","{{(}}","{{1}}","{{+}}","\\frac{1}{n}","\\cdot\\frac{x}{x}",")^{nx}")
        eq5 = MathTex("{{e}}","^{x}", "=","{{(}}","{{1}}","{{+}}","\\frac{x}{nx}",")^{nx}")
        sub1 = MathTex("let\; ","{{\omega}}","=","{{nx}}").next_to(eq5,UP,buff=1)
        eq6 = MathTex("{{e}}","^{x}", "=","{{(}}","{{1}}","{{+}}","\\frac{x}{\\omega}",")^{\\omega}")
        sub2 = MathTex("{{x}}=i{{\\theta}}").next_to(eq6,UP,buff=1)
        eq7 =  MathTex("{{e}}","^{i\\theta}", "=","{{(}}","{{1}}","{{+}}","\\frac{i\\theta}{\\omega}",")^{\\omega}")
        eq8 =  MathTex("{{e}}","^{i\\theta}", "=","{{(}}","{{1}}","{{+}}","i","\\frac{\\theta}{\\omega}",")^{\\omega}")
        limit2= MathTex("\\because \; {{n}}\\to\infty\; \\therefore \;{{\omega}}\\to\infty \; \wedge \;\\frac{1}{\omega}\\to 0").next_to(eq6,UP,buff=.5)
        limit3 = MathTex("\\lim_{\\frac{1}{\\omega}\\to 0").next_to(eq6,UP,buff=.5)
        eq9 =  MathTex("{{e}}","^{i\\theta}", "=","{{[}}","{{\\cos(}}","\\frac{\\theta}{\\omega}","{{)}}","{{+}}","i","{{sin(}}","\\frac{\\theta}{\\omega}","{{)}}","]^{\\omega}")




        lbCos = MathTex('\\cos(\\alpha)').shift(UL*2)
        lbSin = MathTex('\\sin(\\alpha)').shift(DL*2)
        
        xrange = [0,2*PI,PI/4]
        yrange = [-1.5,1.5,.25]
        
        cosPlane = NumberPlane(xrange,yrange,3,2,color=DARK_BLUE,fill_opacity=.5).next_to(lbCos,RIGHT,buff=1)
        sinPlane = NumberPlane(xrange,yrange,3,2,color=DARK_BLUE,fill_opacity=.5).next_to(lbSin,RIGHT,buff=1)
        cosFunc = cosPlane.plot(lambda x: cos(x),x_range=xrange,color=YELLOW)
        sinFunc = sinPlane.plot(lambda x: sin(x),x_range=xrange,color=YELLOW)

        alpha = ValueTracker(TAU)
        dotCos = always_redraw(lambda : Dot().move_to(cosPlane.c2p(alpha.get_value(),cosFunc.underlying_function(alpha.get_value()))))
        dotCosLines = always_redraw(lambda : cosPlane.get_lines_to_point(cosPlane.c2p(alpha.get_value(),cosFunc.underlying_function(alpha.get_value()))))
        dotSin = always_redraw(lambda : Dot().move_to(sinPlane.c2p(alpha.get_value(),sinFunc.underlying_function(alpha.get_value()))))
        dotSinLines = always_redraw(lambda : sinPlane.get_lines_to_point(sinPlane.c2p(alpha.get_value(),sinFunc.underlying_function(alpha.get_value()))))
        alphaLb = always_redraw(lambda : MathTex("\\alpha = " + str(round(alpha.get_value(),3)) + "\\;\\;\\;\\cos("+str(round(alpha.get_value(),3))+") = "+str(round(cos(alpha.get_value()),3))+"\\;\\;\\;\\sin("+str(round(alpha.get_value(),3))+") = "+str(round(sin(alpha.get_value()),3))))
        
        
        
        
        title2= Text("Demoivre's theorem:").to_edge(UL,buff=1)

        z = MathTex("{{z}}","=","{{r}}","[","\\cos(","{{\\theta}}",")","+","i\\sin(","{{\\theta}}",")","]")
        zN = MathTex("{{z}}","^{n}","=","{{r}}","^{n}","[","\\cos(","{{n}}","{{\\theta}}",")","+","i\\sin(","{{n}}","{{\\theta}}",")","]")
        



        eq10 =  MathTex("{{e}}","^{i\\theta}", "=","(","{{\\cos(}}","\\frac{\\omega \\theta}{\\omega}","{{)}}","+","i","{{\\sin(}}","\\frac{\\omega\\theta}{\\omega}","{{)}}",")^{\\not{\\omega}}")
        eq11 = MathTex("{{e}}","^{i\\theta}", "=","[","{{\\cos(}}","\\frac{\\not{\\omega}\\theta}{\\not{\\omega}}","{{)}}","+","i","{{\\sin(}}","\\frac{\\not{\\omega}\\theta}{\\not{\\omega}}","{{)}}","]")
        eq12 = MathTex("{{e}}","^{i\\theta}", "=","{{\\cos(}}","{{\\theta}}","{{)}}","+","i","{{\\sin(}}","{{\\theta}}",")")

        eq13 = MathTex("{{e}}","^{i\\pi}", "=","{{\\cos(}}","{{\\pi}}","{{)}}","+","i","{{\\sin(}}","{{\\pi}}",")")
        eq14 = MathTex("{{e}}","^{i\\pi}", "=","{{-1}}","+","i","0")
        eq15 = MathTex("{{e}}","^{i\\pi}", "+","{{1}}","=","0")
        
        
        self.play(Write(VGroup(title,eq0)),run_time=2.5)
        self.wait(2.5)
        self.play(FadeOut(VGroup(title,eq0)))
        self.play(Write(VGroup(eq1,limit1)), run_time=2.5)
        self.play(limit1.animate.to_corner(UR,buff=1))
        self.play(TransformMatchingTex(eq1,eq2))
        self.wait(2.5)
        self.play(TransformMatchingTex(eq2,eq3))
        self.wait(2.5)
        self.play(TransformMatchingTex(eq3,eq4))
        self.wait(2.5)
        self.play(TransformMatchingTex(eq4,eq5))
        self.wait(2.5)
        self.play(Write(sub1))
        self.play(TransformMatchingTex(eq5,eq6),sub1.animate.to_edge(UL,buff=1),run_time=1)
        self.wait(2.5)
        self.play(Write(sub2))
        self.wait(2.5)
        self.play(sub2.animate.shift(LEFT * 5.5),TransformMatchingTex(eq6,eq7))
        self.wait(2.5)
        self.play(TransformMatchingTex(eq7,eq8))
        self.wait(2.5)
        self.play(Write(limit2))
        self.wait(2.5)
        self.play(Transform(limit2,limit3))
        self.wait(2.5)
        self.play(limit2.animate.shift(RIGHT * 5.6),limit3.animate.shift(RIGHT * 5.6))
        self.wait(2.5)
        self.play(FadeOut(VGroup(eq8,sub1,sub2,limit1,limit2,limit3)))
        self.wait(2.5)
        self.play(DrawBorderThenFill(VGroup(lbCos,lbSin,cosPlane,sinPlane,cosFunc,sinFunc)))
        self.wait(2.5)
        self.play(Create(VGroup(dotCos,dotCosLines,dotSin,dotSinLines,alphaLb)))
        self.wait(2.5)
        self.play(alpha.animate.set_value(0),run_time=5,rate_func=smooth)
        self.wait(2.5)
        self.play(FadeOut(VGroup(lbCos,lbSin,cosPlane,sinPlane,cosFunc,sinFunc,dotCos,dotCosLines,dotSin,dotSinLines,alphaLb)),FadeIn(VGroup(eq8,sub1,sub2,limit1,limit3)))
        self.wait(2.5)
        self.play(TransformMatchingTex(eq8,eq9))
        self.wait(2.5)
        self.play(FadeOut(VGroup(eq9,sub1,sub2,limit1,limit3)))
        self.wait(2.5)
        self.play(Write(title2))
        self.wait(2.5)
        self.play(Write(z))
        self.wait(2.5)
        self.play(z.animate.shift(UP),Write(zN))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title2,z,zN)),FadeIn(VGroup(eq9,sub1,sub2,limit1,limit3)))
        self.wait(2.5)
        self.play(TransformMatchingTex(eq9,eq10))
        self.wait(2.5)
        self.play(TransformMatchingTex(eq10,eq11))
        self.wait(2.5)
        self.play(TransformMatchingTex(eq11,eq12),FadeOut(VGroup(sub1,sub2,limit1,limit3)))
        self.wait(2.5)
        self.play(TransformMatchingTex(eq12,eq13))
        self.wait(2.5)
        self.play(TransformMatchingTex(eq13,eq14))
        self.wait(2.5)
        self.play(TransformMatchingTex(eq14,eq15))
        self.wait(2.5)
