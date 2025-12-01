


g-log:
	$(T)git log

g-ac:
	$(T)git add *
	$(T)git commit --signoff

TARGETS += g-log g-ac
