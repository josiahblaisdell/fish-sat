df = data.frame(read.csv(".\\results.csv",header = TRUE));
df_clean <- subset(df,df$time < 5000);
df_nexpr_nconstrn = df_clean[,c(1,4,7)];
df_nvar_nconstrn = df_clean[,c(2,5,7)];
df_nvar_nexpr = df_clean[,c(3,6,7)];

df_plot1 <- ggplot(df_clean, aes(x=num_constr, y=time, group=num_vars)) + 
  geom_line(aes(colour=num_vars)) + 
  facet_grid(num_expr ~ .)

ggplot(data=df_nexpr_nconstrn,aes(x=df_nexpr_nconstrn$nvar,y=df_nexpr_nconstrn$time)) +
  geom_line(aes(colour=df_nexpr_nconstrn$lbl_nexpr_nconstr)) +
  labs(title = "Runtime as a function of Number of Constraints") +
  xlab("Number of Constraints") +
  ylab("Runtime (MS)")

ggplot(data=df_nvar_nconstrn,aes(x=df_nvar_nconstrn$nexpr,y=df_nvar_nconstrn$time)) + 
  geom_line(aes(colour=df_nvar_nconstrn$lbl_nvar_nconstrn)) +
  

ggplot(data=df_nvar_nexpr,aes(x=df_nvar_nexpr$nconstrn,y=df_nvar_nexpr$time)) + geom_line(aes(colour=df_nvar_nexpr$lbl_nvar_nexpr))