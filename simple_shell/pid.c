int main(void)
{
	pid_t new_pid;

	new_pid = getpid();
	print("%u\n" , new_pid);
	return(0);
}
