


g-log:
	$(T)git log

g-acp:
	$(T)git add *
	$(T)git commit --signoff
	$(T)git push

TARGETS += g-log g-acp
